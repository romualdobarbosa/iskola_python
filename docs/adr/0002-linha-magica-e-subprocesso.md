# 0002. Linha mágica e um subprocesso por caso

Status: aceito (2026-10-23)

## Contexto

O público já programa em outra linguagem, mas ainda não conhece o jeito Python. Pedir uma função `main()` ou um comando especial pra rodar os testes atrapalha o primeiro contato.

## Decisão

Cada template tem, logo depois do enunciado, a linha `from iskola import verificar; verificar(__file__)`.

- No processo pai, `verificar` roda o próprio arquivo num subprocesso por caso de teste (mesmo interpretador, o do `.venv`), mostra o veredito e encerra com `SystemExit`. O código do aluno nunca roda no pai.
- No subprocesso, marcado pela variável `ISKOLA_SUBPROCESSO`, `verificar` só instala um `excepthook` e retorna. O código do aluno roda como script puro, lendo `input()` e escrevendo com `print()`.
- O `excepthook` extrai a exceção com `rich.traceback.Traceback.extract`, filtra os frames pro arquivo do aluno e grava o `Trace` com pickle no caminho da variável `ISKOLA_ERRO`. O pai desenha o traceback com o rich.
- O subprocesso importa o mínimo (o rich só é importado se der exceção), pra não pesar no tempo de cada caso.
- A raiz do projeto é achada subindo a partir do arquivo até uma pasta com `problemas/` e `testes/`. O problema é achado pelo prefixo numérico do nome do arquivo.

## Consequências

- Funciona igual com `uv run treino/NNN.py` e com o play da IDE, desde que o interpretador seja o `.venv`.
- O aluno não precisa saber o que é função até o 076.
- Erro de sintaxe no arquivo do aluno não passa pelo corretor: o Python não consegue compilar o arquivo, então a linha mágica nunca roda. Aparece a mensagem padrão do Python, que no 3.13 já é boa.
- Os gabaritos não têm a linha mágica. O `iskola validar` chama o corretor direto.
- A linha mágica tem dois comandos separados por ponto e vírgula. Por isso `problemas/` fica fora do `ruff format` e ignora E702 e I001.
