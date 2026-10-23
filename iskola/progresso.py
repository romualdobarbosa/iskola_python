"""O que o aluno já passou, guardado em .iskola/progresso.json."""

import json
from datetime import datetime
from enum import StrEnum
from pathlib import Path


class Status(StrEnum):
    ACEITO = "aceito"
    FALHOU = "falhou"
    PENDENTE = "pendente"


class Progresso:
    def __init__(self, raiz: Path) -> None:
        self.caminho = raiz / ".iskola" / "progresso.json"
        self.problemas: dict[str, dict] = {}
        if self.caminho.exists():
            self.problemas = json.loads(self.caminho.read_text("utf-8")).get(
                "problemas", {}
            )

    def status(self, codigo: str) -> Status:
        registro = self.problemas.get(codigo)
        if not registro:
            return Status.PENDENTE
        return Status.ACEITO if registro["aprovacoes"] else Status.FALHOU

    def registrar(self, codigo: str, aceito: bool) -> None:
        # As datas de aprovação ficam todas guardadas pra revisão espaçada (v2).
        registro = self.problemas.setdefault(
            codigo, {"tentativas": 0, "aprovacoes": []}
        )
        registro["tentativas"] += 1
        if aceito:
            registro["aprovacoes"].append(datetime.now().isoformat(timespec="seconds"))
        self.caminho.parent.mkdir(exist_ok=True)
        conteudo = {"versao": 1, "problemas": self.problemas}
        self.caminho.write_text(
            json.dumps(conteudo, indent=2, ensure_ascii=False), "utf-8"
        )
