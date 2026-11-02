"""Junta tudo quando o aluno roda o arquivo: corrige, grava o progresso e mostra o veredito."""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from iskola import catalogo, mensagens, relatorio
from iskola.catalogo import Problema, ProblemaNaoEncontrado, RaizNaoEncontrada
from iskola.correcao import Resultado, avaliar, falhas
from iskola.progresso import Progresso, Status


def corrigir(arquivo: str) -> int:
    console = Console(highlight=False)
    caminho = Path(arquivo).resolve()
    try:
        problema = catalogo.do_arquivo(caminho)
    except RaizNaoEncontrada:
        console.print(mensagens.SEM_RAIZ.format(pasta=caminho.parent), style="red")
        return 2
    except ProblemaNaoEncontrado:
        console.print(mensagens.SEM_TESTES.format(arquivo=caminho.name), style="red")
        return 2
    if problema.modo != "stdio":
        console.print(
            mensagens.MODO_NAO_SUPORTADO.format(modo=problema.modo), style="red"
        )
        return 2

    total = len(problema.casos)
    with console.status("") as status:
        resultados = avaliar(
            caminho,
            problema,
            lambda i: status.update(mensagens.RODANDO.format(i=i, total=total)),
        )
    passou = next(falhas(resultados), None) is None

    if caminho.parent != problema.raiz / "treino":
        _mostrar(problema, resultados, passou, None, console)
        if caminho.parent == problema.raiz / "problemas":
            _avisar_template(problema, console)
        return 0 if passou else 1

    progresso = Progresso(problema.raiz)
    fase_antes = _aceitos_na_fase(problema, progresso)
    progresso.registrar(problema.codigo, passou)
    _mostrar(problema, resultados, passou, progresso, console)
    fase = problema.fase
    if passou and fase_antes < fase.tamanho == _aceitos_na_fase(problema, progresso):
        relatorio.fase_concluida(fase, console)
    return 0 if passou else 1


def _avisar_template(problema: Problema, console: Console) -> None:
    """Fecha a saída com o aviso, pra ele ser a última coisa na tela."""
    texto = mensagens.AVISO_TEMPLATE.format(arquivo=f"{problema.nome}.py")
    console.print()
    console.print(
        Panel(
            texto,
            title=mensagens.AVISO_TEMPLATE_TITULO,
            title_align="left",
            border_style="bold yellow",
        )
    )


def _mostrar(
    problema: Problema,
    resultados: list[Resultado],
    passou: bool,
    progresso: Progresso | None,
    console: Console,
) -> None:
    if not passou:
        relatorio.falha(problema, resultados, console)
        return
    todos = catalogo.listar(problema.raiz)
    aceitos = _aceitos_na_fase(problema, progresso) if progresso else 0
    relatorio.aceito(
        problema, resultados, aceitos, _proximo(problema, todos, progresso), console
    )


def _aceitos_na_fase(problema: Problema, progresso: Progresso) -> int:
    fase = problema.fase
    return sum(
        progresso.status(f"{n:03}") == Status.ACEITO
        for n in range(fase.inicio, fase.fim + 1)
    )


def _proximo(
    atual: Problema, todos: list[Problema], progresso: Progresso | None
) -> Problema | None:
    """O primeiro depois do atual que ainda não passou; se não houver, o primeiro antes."""
    pendentes = [
        p
        for p in todos
        if p.numero != atual.numero
        and (progresso is None or progresso.status(p.codigo) != Status.ACEITO)
    ]
    depois = [p for p in pendentes if p.numero > atual.numero]
    return (depois or pendentes or [None])[0]
