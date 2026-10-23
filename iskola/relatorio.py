"""Desenha os vereditos no terminal com o rich."""

from difflib import SequenceMatcher

from rich import box
from rich.align import Align
from rich.console import Console, Group, RenderableType
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table
from rich.text import Text
from rich.traceback import Traceback

from iskola import mensagens
from iskola.catalogo import Fase, Problema
from iskola.correcao import LIMITE_SEGUNDOS, Resultado, Veredito

CORES = {
    Veredito.ACEITO: "green",
    Veredito.RESPOSTA_ERRADA: "red",
    Veredito.ERRO_APRESENTACAO: "yellow",
    Veredito.TEMPO_LIMITE: "magenta",
    Veredito.ERRO_EXECUCAO: "dark_orange",
}
MAX_LINHAS_DIFF = 20


def placar(resultados: list[Resultado]) -> Text:
    texto = Text()
    for r in resultados:
        texto.append(
            "✓ " if r.veredito == Veredito.ACEITO else "✗ ", style=CORES[r.veredito]
        )
    aceitos = sum(r.veredito == Veredito.ACEITO for r in resultados)
    texto.append(" " + mensagens.PLACAR.format(aceitos=aceitos, total=len(resultados)))
    return texto


def cabecalho(
    problema: Problema, veredito: Veredito, resultados: list[Resultado]
) -> Panel:
    linha = Text.assemble(
        (mensagens.VEREDITOS[veredito], f"bold {CORES[veredito]}"),
        "   ",
        placar(resultados),
    )
    return Panel(
        linha, title=_titulo(problema), title_align="left", border_style=CORES[veredito]
    )


def falha(problema: Problema, resultados: list[Resultado], console: Console) -> None:
    indice, primeira = next(
        (i, r) for i, r in enumerate(resultados, 1) if r.veredito != Veredito.ACEITO
    )
    v = primeira.veredito
    console.print(cabecalho(problema, v, resultados))
    console.print(mensagens.EXPLICACOES[v].format(limite=_numero(LIMITE_SEGUNDOS)))
    console.print()
    console.print(
        Text(mensagens.CASO.format(i=indice, total=len(resultados)), style="bold")
    )
    console.print(_entrada(primeira.caso.entrada))

    if v in (Veredito.RESPOSTA_ERRADA, Veredito.ERRO_APRESENTACAO):
        console.print(diff(primeira.caso.saida, primeira.obtido, CORES[v]))
    elif v == Veredito.ERRO_EXECUCAO:
        _erro_execucao(primeira, console)

    console.print()
    caminho = problema.dica.relative_to(problema.raiz).as_posix()
    console.print(mensagens.TRAVOU.format(caminho=caminho), style="bold")


def aceito(
    problema: Problema,
    resultados: list[Resultado],
    aceitos_na_fase: int,
    proximo: Problema | None,
    console: Console,
) -> None:
    fase = problema.fase
    tempo = max(r.tempo for r in resultados)
    barra = Table.grid(padding=(0, 2))
    barra.add_row(
        fase.nome,
        ProgressBar(total=fase.tamanho, completed=aceitos_na_fase, width=24),
        f"{aceitos_na_fase}/{fase.tamanho}",
    )
    partes: list[RenderableType] = [
        Text.assemble(
            (mensagens.VEREDITOS["aceito"], "bold green"), "   ", placar(resultados)
        ),
        Text(mensagens.TEMPO.format(tempo=_numero(tempo)), style="dim"),
        Text(),
        barra,
        Text(),
    ]
    if proximo:
        partes.append(
            Text(mensagens.PROXIMO.format(codigo=proximo.codigo, titulo=proximo.titulo))
        )
        partes.append(
            Text(mensagens.COMANDO_RODAR.format(nome=proximo.nome), style="cyan")
        )
    else:
        partes.append(Text(mensagens.FIM_DOS_PROBLEMAS))
    console.print(
        Panel(
            Group(*partes),
            title=_titulo(problema),
            title_align="left",
            border_style="green",
            padding=(1, 2),
        )
    )


def fase_concluida(fase: Fase, console: Console) -> None:
    texto = Group(
        Align.center(
            Text(mensagens.FASE_CONCLUIDA.format(nome=fase.nome), style="bold green")
        ),
        Align.center(Text(mensagens.FASE_CONCLUIDA_DETALHE.format(total=fase.tamanho))),
    )
    console.print(Panel(texto, box=box.DOUBLE, border_style="green", padding=(1, 4)))


def diff(esperado: str, obtido: str, cor: str) -> Table:
    """Tabela linha a linha, com os caracteres diferentes em destaque."""
    lado_e, lado_o = _linhas(esperado), _linhas(obtido)
    total = max(len(lado_e), len(lado_o), 1)
    primeira = next(
        (i for i in range(total) if _linha(lado_e, i) != _linha(lado_o, i)), 0
    )
    inicio = max(0, primeira - 5) if total > MAX_LINHAS_DIFF else 0
    fim = min(total, inicio + MAX_LINHAS_DIFF)

    tabela = Table(box=box.ROUNDED, show_lines=False, header_style="bold")
    tabela.add_column("", style="dim", justify="right")
    tabela.add_column(mensagens.ESPERADO)
    tabela.add_column(mensagens.OBTIDO)
    for i in range(inicio, fim):
        e, o = _linha(lado_e, i), _linha(lado_o, i)
        trechos_e, trechos_o = _trechos_diferentes(e, o)
        tabela.add_row(
            Text(str(i + 1), style=cor if e != o else "dim"),
            _visivel(e, trechos_e, "bold black on green"),
            _visivel(o, trechos_o, f"bold white on {cor}")
            if obtido or i > 0
            else Text(mensagens.NADA, style="dim"),
        )
    if fim < total:
        tabela.add_row(
            "", Text(mensagens.LINHAS_OCULTAS.format(n=total - fim), style="dim"), ""
        )
    return tabela


# Cada linha é (conteúdo, terminou com quebra?) ou None quando o lado não tem essa linha.
Linha = tuple[str, bool] | None


def _linhas(texto: str) -> list[tuple[str, bool]]:
    partes = texto.split("\n")
    linhas = [(p, True) for p in partes[:-1]]
    if partes[-1]:
        linhas.append((partes[-1], False))
    return linhas


def _linha(linhas: list[tuple[str, bool]], i: int) -> Linha:
    return linhas[i] if i < len(linhas) else None


def _trechos_diferentes(e: Linha, o: Linha) -> tuple[set[int], set[int]]:
    """Posições a destacar em cada lado. A posição len(conteúdo) é a quebra de linha."""
    if e is None or o is None:
        lado = e or o
        tudo = set(range(len(lado[0]) + 1)) if lado else set()
        return (tudo, set()) if o is None else (set(), tudo)
    texto_e, texto_o = e[0], o[0]
    trechos_e: set[int] = set()
    trechos_o: set[int] = set()
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, texto_e, texto_o).get_opcodes():
        if tag != "equal":
            trechos_e.update(range(i1, i2))
            trechos_o.update(range(j1, j2))
    if e[1] != o[1]:
        (trechos_e if e[1] else trechos_o).add(len(texto_e if e[1] else texto_o))
    return trechos_e, trechos_o


def _visivel(linha: Linha, destaque: set[int], estilo: str) -> Text:
    texto = Text()
    if linha is None:
        return texto
    conteudo, quebra = linha
    for i, caractere in enumerate(conteudo):
        estilo_base = "dim" if caractere == " " else ""
        texto.append(
            "·" if caractere == " " else caractere,
            estilo if i in destaque else estilo_base,
        )
    if quebra:
        texto.append("⏎", estilo if len(conteudo) in destaque else "dim")
    return texto


def _entrada(entrada: str) -> RenderableType:
    if not entrada:
        return Text.assemble((mensagens.ENTRADA, "bold"), " ", (mensagens.VAZIA, "dim"))
    corpo = entrada.removesuffix("\n")
    return Panel(Text(corpo), title=mensagens.ENTRADA, title_align="left", expand=False)


def _erro_execucao(resultado: Resultado, console: Console) -> None:
    if resultado.trace is None:
        if resultado.stderr.strip():
            console.print(Text(resultado.stderr.rstrip()))
        codigo = resultado.codigo_saida
        console.print(
            mensagens.SAIU_COM_CODIGO.format(codigo=codigo), style="dark_orange"
        )
        return
    console.print(Traceback(resultado.trace, width=console.width, word_wrap=True))
    # A primeira pilha é a exceção que derrubou o programa; as outras são as causas.
    tipo = resultado.trace.stacks[0].exc_type
    explicacao = mensagens.EXCECOES.get(
        tipo, mensagens.EXCECAO_GENERICA.format(tipo=tipo)
    )
    console.print(Text(explicacao, style=CORES[Veredito.ERRO_EXECUCAO]))


def _titulo(problema: Problema) -> str:
    return mensagens.TITULO_PROBLEMA.format(
        codigo=problema.codigo, titulo=problema.titulo
    )


def _numero(valor: float) -> str:
    return f"{valor:.2f}".replace(".", ",") if valor % 1 else f"{valor:.0f}"
