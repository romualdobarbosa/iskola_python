# Dica do 013 · Conta do restaurante

O float guarda os números em binário, e 0.1 não tem representação exata em binário, do mesmo jeito que 1/3 não tem em decimal. Por isso uma soma que deveria dar 127.50 pode sair 127.49999999999999. O round do Python também não arredonda como a escola quando o número cai bem no meio. Ele usa outra regra, que tem nome. Dois caminhos funcionam aqui. Um é limpar o lixo do float antes de arredondar. O outro é nem deixar o lixo aparecer, trabalhando com inteiros.

## Termos que valem uma pesquisa

- aritmética de ponto flutuante e seus problemas
- arredondamento bancário (meio pro par)
- a função round

## Leitura

- [Aritmética de ponto flutuante, problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html)
- [A função round](https://docs.python.org/pt-br/3/library/functions.html#round)
