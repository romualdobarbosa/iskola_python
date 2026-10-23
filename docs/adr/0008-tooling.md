# 0008. Tooling

Status: aceito (2026-10-23)

## Decisão

- Projeto uv. Nome no pyproject `iskola-python`, pacote `iskola`, comando `iskola`. Build com `uv_build`, layout plano (`module-root = ""`).
- Python 3.13 pinado em `.python-version`. O uv baixa, sem depender do Python do sistema.
- Dependência única, rich. Dev, ruff e pre-commit.
- pre-commit com `ruff check`, `ruff format` e `iskola validar`. O ruff ignora `treino/`.
- Workflow do GitHub Actions em `.github/workflows/ci.yml`, pra quando houver remoto.
- CLI: `iskola` (mapa, copia templates novos pro `treino/` sem sobrescrever), `iskola resetar NNN` (a versão anterior vai pra `.iskola/lixeira/`) e `iskola validar`.

## Consequências

O ruff 0.17 já vem com bem mais regras ativas por padrão. O projeto segue esse padrão em vez de escolher regras.
