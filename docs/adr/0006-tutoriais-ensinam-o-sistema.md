# 0006. Os tutoriais ensinam o sistema junto com a sintaxe

Status: aceito (2026-10-23)

## Decisão

Os seis primeiros problemas ensinam uma sintaxe e uma parte do corretor cada. Quando o objetivo é mostrar um veredito, o template já vem com o erro que provoca esse veredito.

| # | Sintaxe | Parte do sistema | Template |
|---|---|---|---|
| 001 | `print` | ler o diff, Resposta Errada → Aceito | `print("ola mundo")` |
| 002 | `input()` | vários casos, entrada, placar | vazio |
| 003 | `print` (sep, end, f-string) | Erro de Apresentação | `print(sobrenome + ", ", nome)` |
| 004 | `if` + `int()` | Erro de Execução, pasta `dicas/` | compara `input()` direto com 16 |
| 005 | `for` + `range` | mapa (`uv run iskola`) | vazio |
| 006 | `while` | Tempo Limite Excedido, pasta `solucoes/` | `n // 2` sem atribuir |

## Consequências

O primeiro run de 001, 003, 004 e 006 nunca dá Aceito, e isso é o esperado. O 006 leva uns 6 segundos no primeiro run (três casos estourando 2 s), com um spinner mostrando o caso.
