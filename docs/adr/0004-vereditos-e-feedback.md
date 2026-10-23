# 0004. Vereditos e o que cada falha mostra

Status: aceito (2026-10-23)

## Contexto

O pilar do feedback do erro pede que a falha diga exatamente o que deu errado, sem soterrar o aluno.

## Decisão

Cinco vereditos, cada um com uma cor.

| Veredito | Cor | Quando |
|---|---|---|
| Aceito | verde | saída idêntica em todos os casos |
| Resposta Errada | vermelho | saída diferente |
| Erro de Apresentação | amarelo | diferença só de espaço ou linha em branco no fim |
| Tempo Limite Excedido | magenta | passou de 2 s num caso |
| Erro de Execução | laranja | o processo terminou com código diferente de 0 |

- Todos os casos rodam e o placar mostra um ✓ ou ✗ por caso, mas só a primeira falha é detalhada (entrada, esperado, obtido).
- O diff é uma tabela linha a linha. Espaço aparece como `·`, quebra de linha como `⏎`, e os caracteres diferentes ficam em destaque. Saída grande mostra uma janela de 20 linhas a partir da primeira diferença.
- Erro de Execução mostra o traceback do rich filtrado pro arquivo do aluno, mais uma frase em português sobre o tipo da exceção (`mensagens.EXCECOES`). Se o processo saiu com código diferente de 0 sem exceção (um `exit(3)`), mostra o código.
- Toda falha termina com "Travou? Veja dicas/NNN_slug.md".
- Aceito mostra um painel com o tempo do caso mais lento, a barra de progresso da fase e o próximo problema. Fechar uma fase dá um banner maior, com borda dupla.
- A saída do aluno é lida até 1 MB, pra um loop infinito com print não estourar a memória.

## Consequências

O título do painel do traceback ("Traceback (most recent call last)") e a mensagem original da exceção continuam em inglês, porque vêm do rich e do Python. A frase em português embaixo cobre isso.
