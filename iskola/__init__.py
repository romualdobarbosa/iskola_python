"""Ambiente de drills de Python com feedback no terminal."""

import os

# Marca o processo filho que roda um caso de teste. Lá, verificar() não corrige nada.
VARIAVEL_SUBPROCESSO = "ISKOLA_SUBPROCESSO"
# Arquivo onde o processo filho grava a exceção que derrubou o código do aluno.
VARIAVEL_ERRO = "ISKOLA_ERRO"


def verificar(arquivo: str) -> None:
    """Corrige o arquivo do aluno contra os testes e encerra o processo.

    Dentro do subprocesso de um caso de teste não corrige nada: só prepara a captura de
    exceções e devolve o controle, pro código do aluno rodar como script puro.
    """
    if os.environ.get(VARIAVEL_SUBPROCESSO):
        from iskola.captura import instalar

        instalar(arquivo)
        return

    from iskola.harness import corrigir

    raise SystemExit(corrigir(arquivo))
