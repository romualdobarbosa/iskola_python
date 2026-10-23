"""Onde ficam os problemas, os testes e as fases."""

import tomllib
from dataclasses import dataclass
from pathlib import Path

from iskola import mensagens

TOTAL = 100


class RaizNaoEncontrada(Exception):
    pass


class ProblemaNaoEncontrado(Exception):
    pass


@dataclass(frozen=True)
class Fase:
    nome: str
    inicio: int
    fim: int

    def __contains__(self, numero: int) -> bool:
        return self.inicio <= numero <= self.fim

    @property
    def tamanho(self) -> int:
        return self.fim - self.inicio + 1


_FAIXAS = [(1, 6), (7, 22), (23, 35), (36, 50), (51, 65), (66, 75), (76, 82), (83, 100)]
FASES = [
    Fase(nome, inicio, fim) for nome, (inicio, fim) in zip(mensagens.FASES, _FAIXAS)
]


@dataclass(frozen=True)
class Caso:
    entrada: str
    saida: str
    pesado: bool = False


@dataclass(frozen=True)
class Problema:
    raiz: Path
    nome: str  # "001_ola_mundo": o prefixo numérico casa as pastas paralelas
    titulo: str
    modo: str
    casos: tuple[Caso, ...]

    @property
    def codigo(self) -> str:
        return self.nome[:3]

    @property
    def numero(self) -> int:
        return int(self.codigo)

    @property
    def fase(self) -> Fase:
        return next(f for f in FASES if self.numero in f)

    @property
    def template(self) -> Path:
        return self.raiz / "problemas" / f"{self.nome}.py"

    @property
    def treino(self) -> Path:
        return self.raiz / "treino" / f"{self.nome}.py"

    @property
    def dica(self) -> Path:
        return self.raiz / "dicas" / f"{self.nome}.md"

    @property
    def solucao(self) -> Path:
        return self.raiz / "solucoes" / f"{self.nome}.md"

    @property
    def gabaritos(self) -> list[Path]:
        pasta = self.raiz / "gabaritos"
        return sorted(
            [*pasta.glob(f"{self.nome}.py"), *pasta.glob(f"{self.nome}.*.py")]
        )


def achar_raiz(inicio: Path) -> Path:
    for pasta in [inicio, *inicio.parents]:
        if (pasta / "testes").is_dir() and (pasta / "problemas").is_dir():
            return pasta
    raise RaizNaoEncontrada(inicio)


def carregar(caminho: Path) -> Problema:
    with open(caminho, "rb") as arquivo:
        dados = tomllib.load(arquivo)
    casos = tuple(
        Caso(c.get("entrada", ""), c["saida"], c.get("pesado", False))
        for c in dados["casos"]
    )
    return Problema(
        raiz=caminho.parent.parent,
        nome=caminho.stem,
        titulo=dados["titulo"],
        modo=dados.get("modo", "stdio"),
        casos=casos,
    )


def listar(raiz: Path) -> list[Problema]:
    return [
        carregar(c) for c in sorted((raiz / "testes").glob("[0-9][0-9][0-9]_*.toml"))
    ]


def do_arquivo(arquivo: Path) -> Problema:
    """Acha o problema de um arquivo pelo prefixo numérico (treino, gabarito ou template)."""
    raiz = achar_raiz(arquivo.parent)
    codigo = arquivo.name[:3]
    candidatos = (
        sorted((raiz / "testes").glob(f"{codigo}_*.toml")) if codigo.isdigit() else []
    )
    if not candidatos:
        raise ProblemaNaoEncontrado(arquivo.name)
    return carregar(candidatos[0])
