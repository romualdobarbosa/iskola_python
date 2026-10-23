# 0003. Dois modos de correção, stdio e funcao

Status: aceito (2026-10-23). Só o `stdio` está implementado.

## Contexto

No começo o aluno ainda não escreveu função. No fim (algoritmos) o natural é testar uma função com argumentos, como no LeetCode.

## Decisão

- `modo = "stdio"` (até perto do 075). Os casos têm `entrada` (stdin) e `saida` (stdout esperado). A comparação é textual e exata. Se a diferença for só de espaço, ou de linha em branco no fim, o veredito é Erro de Apresentação. Float sempre vem com formato exato no enunciado.
- `modo = "funcao"` (076 em diante). O template traz a assinatura tipada, os testes chamam a função com argumentos e comparam o retorno. Não existe Erro de Apresentação nesse modo.

Pra decidir se é Erro de Apresentação, cada linha tem os espaços colapsados (`" ".join(linha.split())`) e as linhas vazias do fim são removidas. Se os dois lados ficarem iguais, é Erro de Apresentação. A falta da quebra de linha final também cai aqui.

## Consequências

O corretor recusa com mensagem clara qualquer modo diferente de `stdio` até o `funcao` ser escrito, antes do 076.
