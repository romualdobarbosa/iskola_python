# 0005. Pastas paralelas casadas pelo número

Status: aceito (2026-10-23)

## Decisão

| Pasta | Conteúdo |
|---|---|
| `problemas/NNN_slug.py` | template, com docstring (enunciado e 1 ou 2 exemplos), linha mágica e área em branco |
| `testes/NNN_slug.toml` | `titulo`, `modo` e os `[[casos]]` (`entrada`, `saida`, `pesado`) |
| `dicas/NNN_slug.md` | estilo OverTheWire, termos pra pesquisar e links da doc oficial, zero código, uma dica só |
| `gabaritos/NNN_slug.py` e `NNN_slug.<variante>.py` | o que o `iskola validar` (e o CI) roda |
| `solucoes/NNN_slug.md` | explicação baseada nos gabaritos, da força bruta à otimizada, com Big-O |
| `treino/` | onde o aluno trabalha (gitignore) |
| `.iskola/progresso.json` | progresso, com as datas de aprovação (gitignore) |

A solução fica em outra pasta de propósito. Ter que ir abrir outra pasta freia o impulso de olhar a resposta.

O `[[casos]]` usa string multilinha do TOML. A quebra de linha logo depois das aspas de abertura é descartada pelo TOML, então

```toml
saida = """
Olá, mundo!
"""
```

vale `"Olá, mundo!\n"`, exatamente o que um `print` produz.

## Consequências

O `iskola validar` confere que cada teste tem template, dica, solução e pelo menos um gabarito.
