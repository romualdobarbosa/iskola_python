# Decisões de design — iskola_python

Fechadas numa sessão de grilling em 2026-10-23. Este arquivo é a fonte até virar
`docs/adr/`, `docs/GLOSSARIO.md` e `docs/CURRICULO.md` (passo 1 da ordem de trabalho).

## Conceito

- Drills de Python estilo URI (começo) e LeetCode (fim). 100 problemas **originais**: o URI
  só inspira, não citamos nem copiamos texto/número. Licença MIT no nome de Romualdo Barbosa.
- PT-BR primeiro. Versão EN depois, para a comunidade. Todo texto de interface fica isolado
  num módulo `mensagens` pra facilitar a tradução.
- Público: quem já programa em outra linguagem e quer aprender a sintaxe e o jeito Python.
  Não ensinamos lógica de programação do zero.
- Base nos pilares da neurociência: atenção, engajamento ativo, feedback do erro e consolidação.
- **Metáfora da solda**: cada problema reaproveita o que o anterior ensinou e expande só um
  passo. Nem difícil demais, nem repetitivo.

## Fases (ponto de partida, ajustável no CURRICULO)

| Faixa   | Fase |
|---------|------|
| 001–006 | Tutorial (sistema + sintaxe básica) |
| 007–022 | Números, operadores, formatação (int, float, bool) |
| 023–035 | Condicionais compostas + laços aplicados (contadores, acumuladores, aninhados) |
| 036–050 | Strings |
| 051–065 | Listas e tuplas (inclui matrizes) |
| 066–075 | Dicionários e sets |
| 076–082 | Funções + mini-intro a classes (transição pro modo `funcao`) |
| 083–100 | Algoritmos: two pointers, sliding window, binary search, stack, linked list |

## Tutoriais — cada um ensina sintaxe + uma parte do sistema

| #   | Sintaxe | Parte do sistema |
|-----|---------|------------------|
| 001 | `print` | Template já vem quase certo (`print("ola mundo")`): o 1º run dá Resposta Errada, o aluno lê o diff, corrige e vê o Aceito |
| 002 | `input()` | Múltiplos casos de teste, o que é "entrada", o placar x/y |
| 003 | `print` (sep, end, f-string) | Erro de Apresentação |
| 004 | `if` + `int()` | Erro de Execução (esquecer o `int()`) + onde ficam as `dicas/` |
| 005 | `for` + `range` | Mapa de progresso (`uv run iskola`) |
| 006 | `while` | Tempo Limite Excedido + onde ficam as `solucoes/` |

## Estrutura de pastas

```
iskola/      pacote: harness, CLI, mensagens
problemas/   NNN_slug.py    template: docstring com enunciado + 1-2 exemplos,
                            linha mágica, área em branco
testes/      NNN_slug.toml  casos + modo (stdio | funcao); casos `pesado = true` a partir do 083
dicas/       NNN_slug.md    estilo OverTheWire: conceitos/termos pra pesquisar + link da doc oficial, ZERO código, dica única (sem níveis)
gabaritos/   NNN_slug.py | NNN_slug.<variante>.py   (ex.: .forca_bruta.py, .otimizada.py) — o que o CI valida
solucoes/    NNN_slug.md    explicação detalhada baseada nos gabaritos; com várias variantes, bruta → otimizada, Big-O de tempo e espaço
treino/      (gitignore) onde o aluno trabalha
.iskola/     (gitignore) progresso.json, com datas de aprovação
docs/        CURRICULO.md, GLOSSARIO.md, adr/
```

As pastas são paralelas e casam pelo prefixo numérico. Solução em pasta separada é de
propósito: ter que ir abrir outra pasta freia o impulso de olhar a resposta.

## Harness

- Topo do arquivo, logo depois do enunciado: `from iskola import verificar; verificar(__file__)`.
  No processo pai, roda o próprio arquivo em subprocesso (mesmo interpretador do venv), um por
  caso de teste, e sai. No subprocesso (marcado por variável de ambiente) não faz nada, e o
  código do aluno roda como script puro. O aluno não precisa saber o que é função.
- **Modo `stdio`** (até ~075): stdin → stdout, comparação textual. Diferença só de espaço ou linha
  em branco no fim = Erro de Apresentação. Float sempre com formato exato no enunciado.
- **Modo `funcao`** (076+): o template traz a assinatura tipada. Os testes chamam com argumentos e
  comparam o retorno. Sem Erro de Apresentação.
- Vereditos: **Aceito** (verde), **Resposta Errada** (vermelho), **Erro de Apresentação**
  (amarelo), **Tempo Limite Excedido** (magenta, 2s por caso, "tem um loop que nunca termina?"),
  **Erro de Execução** (laranja).
- Roda todos os casos e mostra o placar, mas detalha só a primeira falha: entrada, esperado,
  obtido e diff com destaque. Exceção: traceback do rich filtrado pro código do aluno + frase em
  PT explicando o tipo. Toda falha termina com "Travou? Veja `dicas/NNN_slug.md`".
- Aceito: painel do rich com número/título, tempo, barra de progresso da fase e "próximo: …".
  Fechar uma fase dá um banner maior.
- Complexidade (083+): casos `pesado` fazem O(n²) estourar o tempo. O gabarito força bruta
  declara `# iskola: espera_tle`, e o validador confere que ele de fato estoura (prova que o caso
  pesado discrimina).

## CLI

- `uv run iskola`: mapa dos 100 (✅ passou / ⬜ pendente / ❌ tentou e falhou), fase atual e
  próximo recomendado. Copia pro `treino/` todo template que ainda não existe lá, **nunca
  sobrescreve**.
- `iskola resetar NNN`: restaura um arquivo do treino a partir do template.
- `iskola validar`: roda todos os gabaritos contra os testes.
- v2: revisão espaçada (pilar da consolidação), usando as datas que o progresso já grava.

## Tooling

- Projeto uv. Nome no pyproject: `iskola-python`. Pacote importado: `iskola`. Comando: `iskola`.
- Python 3.13 pinado em `.python-version` (o uv baixa, sem depender do Python do usuário).
- Dependência: rich. Dev: ruff, pre-commit.
- pre-commit: `ruff check` + `ruff format` + `iskola validar`. O ruff ignora `treino/`.
- Workflow do GitHub Actions pronto, pra quando houver remoto.
- `git init` na branch `main`. `.gitignore` com `.venv`, `treino/`, `.iskola/`. LICENSE MIT.
- README do aluno: `uv sync` → `uv run iskola` → abrir `treino/001_ola_mundo.py` e rodar com
  `uv run treino/001_ola_mundo.py` ou com o play da IDE (interpretador = `.venv`).
- README e textos públicos passam pela skill `voz-romualdo`.

## Ordem de trabalho

1. **Teste de fogo**: esqueleto + harness + CLI + os 6 tutoriais (com testes, dicas, gabaritos,
   soluções) + docs (adr, glossário). Testar o fluxo inteiro (uv, rich, cada veredito). Aprovação
   do Romualdo → primeiro commit.
2. `docs/CURRICULO.md` com os 100: título, conceito **novo**, conceito **soldado** do anterior.
   O Romualdo manda problemas do URI que curtiu pra inspirar e revisa a progressão.
3. Problemas 007–100 em lotes.
