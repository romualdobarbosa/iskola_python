# iskola_python

Ambiente de drills de Python com feedback colorido no terminal. Todas as decisões de design
estão em `docs/DECISOES.md`. Leia esse arquivo antes de qualquer trabalho aqui.

## Estado atual

- Teste de fogo aprovado pelo Romualdo em 2026-10-23 e commitado (esqueleto, harness, CLI, 6 tutoriais, ADRs, glossário).
- A pasta foi renomeada de `python_iskola` pra `iskola_python`. Se existir um `.venv` criado
  antes do rename, rode `rm -rf .venv && uv sync`.
- Currículo dos 100 aprovado em 2026-10-23 (`docs/CURRICULO.md`). A coluna "Soldado" diz de qual problema
  anterior cada um depende; respeite isso ao escrever.
- **Próximo passo**: item 3 da "Ordem de trabalho", escrever os problemas em lotes, uma fase por sessão,
  começando por 007–022. Cada problema vem completo (template, teste, dica, gabarito, solução) e o
  `iskola validar` tem que passar. Antes do 076, implementar o modo `funcao` (ver "Pendências" no currículo).
