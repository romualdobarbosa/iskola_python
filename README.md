# iskola_python

Drills de Python com correção no terminal, no estilo dos juízes online. Você escreve o código, roda o arquivo e o corretor responde na hora com um veredito colorido, mostrando o que esperava, o que recebeu e onde os dois diferem.

Fiz pra quem já programa em outra linguagem e quer aprender a sintaxe e o jeito Python, então lógica de programação do zero não entra aqui. O plano são 100 problemas, parecidos com os do URI no começo e com os do LeetCode no fim, todos escritos do zero (o URI só serviu de inspiração). Cada problema reaproveita o que o anterior ensinou e avança um passo. Por enquanto estão prontos os 6 tutoriais, e o resto vem em lotes.

## Como começar

Você precisa do [uv](https://docs.astral.sh/uv/). Ele baixa o Python 3.13 sozinho, então não importa qual Python está instalado na sua máquina.

Antes de começar, desligue o autocomplete da sua IDE, principalmente o de IA (o Copilot no VS Code, o assistente do PyCharm e afins). Ele escreve a linha antes de você pensar nela, e o drill existe pra você escrever cada linha com a própria cabeça. Eu desliguei antes de usar. O passo a passo está em [Como desligar o autocomplete](#como-desligar-o-autocomplete).

```
uv sync
uv run iskola
```

O segundo comando mostra o mapa dos problemas e copia os templates pra pasta `treino/`, que é onde você trabalha. Abra `treino/001_ola_mundo.py` e rode assim:

```
uv run treino/001_ola_mundo.py
```

O play da IDE também funciona, desde que o interpretador seja o `.venv` do projeto.

O 001 já vem com uma tentativa quase certa, e o primeiro resultado é Resposta Errada de propósito. Os seis primeiros problemas são tutoriais, e cada um apresenta uma parte do corretor junto com a sintaxe.

## Como desligar o autocomplete

Vale aprender a desligar e a religar, porque fora do drill você provavelmente vai querer ele de volta. Os menus mudam de versão pra versão, então se o caminho abaixo não bater com a sua IDE, a documentação oficial linkada em cada uma está sempre atualizada.

No VS Code, com o Copilot:

- Clique no ícone do Copilot na barra de status (embaixo, à direita) e desmarque as sugestões inline. Dá pra desligar pra tudo ou só pra Python.
- Pra pausar por um tempo, o mesmo menu tem o Snooze, que desliga por 5 minutos a cada clique.
- Pra religar, é o mesmo menu, marcando de novo.
- Documentação oficial: [Inline suggestions from GitHub Copilot in VS Code](https://code.visualstudio.com/docs/editing/ai-powered-suggestions).

No PyCharm:

- Abra as configurações (Ctrl+Alt+S) e vá em Editor › General › Inline Completion. Desmarque as opções de sugestão por linha inteira, local e na nuvem.
- Pra religar, é a mesma tela.
- Documentação oficial: [Use AI in editor](https://www.jetbrains.com/help/pycharm/use-ai-in-editor.html) e [Disable AI Assistant](https://www.jetbrains.com/help/pycharm/disable-ai-assistant.html).

Em outra IDE, procure nas configurações por "inline suggestions", "inline completion" ou pelo nome da extensão de IA.

## Os vereditos

| Veredito | Quando aparece |
|---|---|
| Aceito | a saída bateu em todos os casos de teste |
| Resposta Errada | a saída é diferente da esperada |
| Erro de Apresentação | a resposta está certa, mas sobrou ou faltou espaço ou linha em branco |
| Tempo Limite Excedido | o programa passou de 2 segundos num caso |
| Erro de Execução | o programa quebrou, e o corretor explica o erro em português |

O corretor roda todos os casos e mostra o placar, mas detalha só a primeira falha.

## Onde fica cada coisa

| Pasta | O que tem |
|---|---|
| `treino/` | o seu código |
| `dicas/` | uma dica por problema, sem código, só termos pra pesquisar e links da documentação oficial |
| `solucoes/` | explicação detalhada de cada problema |
| `problemas/` | os templates originais |
| `testes/` | os casos de teste |
| `gabaritos/` | as soluções que validam os testes |

A solução fica numa pasta separada pra dar trabalho ir olhar antes da hora. Depois do Aceito vale abrir e comparar com o seu jeito.

## Comandos

```
uv run iskola                 # mapa e cópia dos templates novos (nunca sobrescreve o seu treino)
uv run iskola resetar 004     # volta treino/004 ao template; a versão anterior vai pra .iskola/lixeira/
uv run iskola validar         # roda todos os gabaritos contra os testes
```

## Pra quem quer mexer no projeto

```
uv sync
uv run pre-commit install
```

O pre-commit roda o ruff e o `iskola validar`. As decisões de design estão em `docs/adr/` e os termos do projeto em `docs/GLOSSARIO.md`.

## Licença

MIT, por Romualdo Barbosa.
