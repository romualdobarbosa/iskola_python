"""Comando iskola: mapa de progresso, resetar e validar."""

import shutil
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from iskola import catalogo, mensagens
from iskola.catalogo import FASES, TOTAL, Problema, RaizNaoEncontrada
from iskola.correcao import Veredito, avaliar
from iskola.progresso import Progresso, Status

# Um gabarito força bruta com esta linha tem que estourar o tempo nos casos pesados.
MARCA_ESPERA_TLE = "# iskola: espera_tle"

console = Console(highlight=False)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    try:
        raiz = catalogo.achar_raiz(Path.cwd())
    except RaizNaoEncontrada:
        raiz = Path(__file__).resolve().parent.parent
    match args:
        case []:
            return mapa(raiz)
        case ["resetar", codigo]:
            return resetar(raiz, codigo)
        case ["validar"]:
            return validar(raiz)
        case _:
            console.print(mensagens.USO)
            return 2


def mapa(raiz: Path) -> int:
    problemas = catalogo.listar(raiz)
    novos = _copiar_templates(problemas)
    progresso = Progresso(raiz)
    por_numero = {p.numero: p for p in problemas}
    proximo = next(
        (p for p in problemas if progresso.status(p.codigo) != Status.ACEITO), None
    )

    tabela = Table.grid(padding=(0, 2))
    tabela.add_column()
    tabela.add_column(justify="right")
    for fase in FASES:
        existentes = [
            por_numero[n] for n in range(fase.inicio, fase.fim + 1) if n in por_numero
        ]
        if not existentes:
            tabela.add_row(
                Text(fase.nome, style="dim"), Text(mensagens.EM_BREVE, style="dim")
            )
            continue
        aceitos = sum(progresso.status(p.codigo) == Status.ACEITO for p in existentes)
        tabela.add_row(Text(fase.nome, style="bold"), f"{aceitos}/{fase.tamanho}")
        itens = Text()
        for p in existentes:
            estilo = "bold reverse" if p is proximo else ""
            itens.append(
                f"{p.codigo} {mensagens.ICONES[progresso.status(p.codigo)]}", estilo
            )
            itens.append("  ")
        tabela.add_row(itens, "")

    total_aceitos = sum(progresso.status(p.codigo) == Status.ACEITO for p in problemas)
    corpo: list = [tabela, Text(), Text(mensagens.LEGENDA, style="dim")]
    console.print(
        Panel(
            Group(*corpo),
            title=mensagens.MAPA_TITULO.format(aceitos=total_aceitos, total=TOTAL),
            title_align="left",
            padding=(1, 2),
        )
    )
    if novos:
        console.print(mensagens.COPIADOS.format(n=novos), style="dim")
    if proximo:
        console.print(
            mensagens.PROXIMO.format(codigo=proximo.codigo, titulo=proximo.titulo)
        )
        console.print(
            f"  {mensagens.COMANDO_RODAR.format(nome=proximo.nome)}", style="cyan"
        )
    else:
        console.print(mensagens.FIM_DOS_PROBLEMAS)
    return 0


def _copiar_templates(problemas: list[Problema]) -> int:
    """Copia pro treino/ os templates que ainda não estão lá. Nunca sobrescreve."""
    novos = 0
    for p in problemas:
        if p.template.exists() and not p.treino.exists():
            p.treino.parent.mkdir(exist_ok=True)
            shutil.copy2(p.template, p.treino)
            novos += 1
    return novos


def resetar(raiz: Path, codigo: str) -> int:
    codigo = codigo.zfill(3)
    problema = next((p for p in catalogo.listar(raiz) if p.codigo == codigo), None)
    if problema is None or not problema.template.exists():
        console.print(mensagens.PROBLEMA_INEXISTENTE.format(codigo=codigo), style="red")
        return 1
    if problema.treino.exists():
        lixeira = raiz / ".iskola" / "lixeira"
        lixeira.mkdir(parents=True, exist_ok=True)
        backup = f"{problema.nome}.{datetime.now():%Y%m%d-%H%M%S}.py"
        shutil.move(problema.treino, lixeira / backup)
        console.print(mensagens.RESETADO_BACKUP.format(backup=backup), style="dim")
    problema.treino.parent.mkdir(exist_ok=True)
    shutil.copy2(problema.template, problema.treino)
    console.print(
        mensagens.RESETADO.format(arquivo=problema.treino.name), style="green"
    )
    return 0


def validar(raiz: Path) -> int:
    tabela = Table(show_header=False, box=None, padding=(0, 2))
    erros = 0
    gabaritos = 0
    for problema in catalogo.listar(raiz):
        for exigido in (problema.template, problema.dica, problema.solucao):
            if not exigido.exists():
                erros += 1
                falta = exigido.relative_to(raiz).as_posix()
                tabela.add_row(
                    problema.nome,
                    Text(mensagens.VALIDAR_FALTA.format(arquivo=falta), "red"),
                )
        if not problema.gabaritos:
            erros += 1
            tabela.add_row(problema.nome, Text(mensagens.VALIDAR_SEM_GABARITO, "red"))
        for gabarito in problema.gabaritos:
            gabaritos += 1
            ok, descricao = _validar_gabarito(gabarito, problema)
            erros += not ok
            tabela.add_row(gabarito.name, Text(descricao, "green" if ok else "red"))
    console.print(tabela)
    if erros:
        console.print(mensagens.VALIDAR_RESUMO_FALHOU.format(n=erros), style="bold red")
        return 1
    console.print(mensagens.VALIDAR_RESUMO_OK.format(n=gabaritos), style="bold green")
    return 0


def _validar_gabarito(gabarito: Path, problema: Problema) -> tuple[bool, str]:
    resultados = avaliar(gabarito, problema)
    if MARCA_ESPERA_TLE in gabarito.read_text("utf-8"):
        if any(r.veredito == Veredito.TEMPO_LIMITE for r in resultados):
            return True, mensagens.VALIDAR_ESPERA_TLE
        return False, mensagens.VALIDAR_NAO_ESTOUROU
    falhas = [
        f"{i}: {mensagens.VEREDITOS[r.veredito]}"
        for i, r in enumerate(resultados, 1)
        if r.veredito != Veredito.ACEITO
    ]
    if falhas:
        return False, f"{mensagens.VALIDAR_FALHOU} ({', '.join(falhas)})"
    return True, mensagens.VALIDAR_OK
