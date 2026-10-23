"""Roda o arquivo do aluno contra cada caso e decide o veredito. Não imprime nada."""

import contextlib
import os
import pickle
import subprocess
import sys
import tempfile
import time
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from rich.traceback import Trace

from iskola import VARIAVEL_ERRO, VARIAVEL_SUBPROCESSO
from iskola.catalogo import Caso, Problema

LIMITE_SEGUNDOS = 2.0
# Um loop infinito com print gera saída sem parar; o resto é descartado.
LIMITE_BYTES = 1_000_000


class Veredito(StrEnum):
    ACEITO = "aceito"
    RESPOSTA_ERRADA = "resposta_errada"
    ERRO_APRESENTACAO = "erro_apresentacao"
    TEMPO_LIMITE = "tempo_limite"
    ERRO_EXECUCAO = "erro_execucao"


@dataclass
class Resultado:
    caso: Caso
    veredito: Veredito
    obtido: str = ""
    tempo: float = 0.0
    trace: Trace | None = None  # exceção do aluno, já filtrada pro arquivo dele
    stderr: str = ""  # quando o processo morre sem exceção capturada
    codigo_saida: int = 0


def rodar_caso(arquivo: Path, caso: Caso) -> Resultado:
    with tempfile.TemporaryDirectory(prefix="iskola-") as pasta:
        caminho_erro = Path(pasta) / "erro.pickle"
        env = {
            **os.environ,
            VARIAVEL_SUBPROCESSO: "1",
            VARIAVEL_ERRO: str(caminho_erro),
            "PYTHONUTF8": "1",
            "PYTHONIOENCODING": "utf-8",
        }
        with (
            open(Path(pasta) / "stdout", "w+b") as stdout,
            open(Path(pasta) / "stderr", "w+b") as stderr,
        ):
            inicio = time.perf_counter()
            try:
                processo = subprocess.run(
                    [sys.executable, str(arquivo)],
                    input=caso.entrada.encode("utf-8"),
                    stdout=stdout,
                    stderr=stderr,
                    timeout=LIMITE_SEGUNDOS,
                    check=False,
                    env=env,
                    cwd=arquivo.parent,
                )
            except subprocess.TimeoutExpired:
                return Resultado(caso, Veredito.TEMPO_LIMITE, tempo=LIMITE_SEGUNDOS)
            tempo = time.perf_counter() - inicio
            stdout.seek(0)
            obtido = _decodificar(stdout.read(LIMITE_BYTES))
            stderr.seek(0)
            erro = _decodificar(stderr.read(LIMITE_BYTES))

        if processo.returncode != 0:
            trace = None
            if caminho_erro.exists():
                with contextlib.suppress(Exception):
                    trace = pickle.loads(caminho_erro.read_bytes())
            return Resultado(
                caso,
                Veredito.ERRO_EXECUCAO,
                obtido,
                tempo,
                trace,
                erro,
                processo.returncode,
            )

    return Resultado(caso, comparar(caso.saida, obtido), obtido, tempo)


def _decodificar(dados: bytes) -> str:
    return dados.decode("utf-8", errors="replace").replace("\r\n", "\n")


def comparar(esperado: str, obtido: str) -> Veredito:
    if obtido == esperado:
        return Veredito.ACEITO
    if _sem_espacos_extras(obtido) == _sem_espacos_extras(esperado):
        return Veredito.ERRO_APRESENTACAO
    return Veredito.RESPOSTA_ERRADA


def _sem_espacos_extras(texto: str) -> list[str]:
    linhas = [" ".join(linha.split()) for linha in texto.split("\n")]
    while linhas and not linhas[-1]:
        linhas.pop()
    return linhas


def avaliar(
    arquivo: Path, problema: Problema, ao_comecar: Callable[[int], None] | None = None
) -> list[Resultado]:
    """Roda todos os casos, em ordem. ao_comecar recebe o número do caso (1, 2, ...)."""
    if problema.modo != "stdio":
        raise NotImplementedError(problema.modo)
    resultados = []
    for i, caso in enumerate(problema.casos, 1):
        if ao_comecar:
            ao_comecar(i)
        resultados.append(rodar_caso(arquivo, caso))
    return resultados


def falhas(resultados: list[Resultado]) -> Iterator[Resultado]:
    return (r for r in resultados if r.veredito != Veredito.ACEITO)
