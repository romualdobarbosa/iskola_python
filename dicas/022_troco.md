# Dica do 022 · Troco

Converta os dois valores pra centavos logo na leitura, multiplicando por 100. Só que a multiplicação também é feita em float, e 0.57 vezes 100 não dá 57 exato, então o jeito de virar inteiro importa. Com tudo em centavos, cada nota ou moeda é uma divisão com quociente e resto, e um for sobre os valores fixos evita escrever a mesma conta treze vezes.

## Termos que valem uma pesquisa

- a função round versus a função int
- a função divmod
- o comando for sobre uma tupla

## Leitura

- [Aritmética de ponto flutuante, problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html)
- [A função divmod](https://docs.python.org/pt-br/3/library/functions.html#divmod)
- [Comandos for](https://docs.python.org/pt-br/3/tutorial/controlflow.html#for-statements)
