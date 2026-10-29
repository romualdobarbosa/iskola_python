# Dica do 018 · Ônibus da excursão

Aqui a divisão tem que arredondar pra cima, porque aluno não fica pra trás. O módulo math tem uma função pra isso, mas ela recebe o resultado da divisão em float, e um float não guarda todos os dígitos de um número tão grande. Existe um truque pra arredondar pra cima usando só divisão inteira. Pense no que acontece se você somar algo a A antes de dividir, ou no que a divisão inteira faz com números negativos.

## Termos que valem uma pesquisa

- a função ceil do módulo math
- divisão inteira arredondando pra cima
- precisão do float com inteiros grandes

## Leitura

- [A função math.ceil](https://docs.python.org/pt-br/3/library/math.html#math.ceil)
- [Operações numéricas](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Aritmética de ponto flutuante, problemas e limitações](https://docs.python.org/pt-br/3/tutorial/floatingpoint.html)
