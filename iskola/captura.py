"""Roda no subprocesso: guarda a exceção do aluno pro processo pai mostrar com o rich."""

import contextlib
import os
import pickle
import sys
from types import TracebackType

from iskola import VARIAVEL_ERRO


def instalar(arquivo: str) -> None:
    destino = os.environ.get(VARIAVEL_ERRO)
    if not destino:
        return
    alvo = os.path.realpath(arquivo)

    def gancho(
        tipo: type[BaseException], valor: BaseException, tb: TracebackType | None
    ) -> None:
        # O gancho nunca pode quebrar; se falhar, o pai mostra o stderr puro.
        with contextlib.suppress(Exception):
            from rich.traceback import Traceback

            trace = Traceback.extract(tipo, valor, tb)
            # Só interessam as linhas do aluno; o resto é ruído pra quem está aprendendo.
            for pilha in trace.stacks:
                do_aluno = [
                    f for f in pilha.frames if os.path.realpath(f.filename) == alvo
                ]
                if do_aluno:
                    pilha.frames = do_aluno
            with open(destino, "wb") as saida:
                pickle.dump(trace, saida)
        sys.__excepthook__(tipo, valor, tb)

    sys.excepthook = gancho
