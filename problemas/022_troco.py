"""
022 · Troco

Leia o valor da compra e o valor pago, um por linha, com duas casas decimais. O
pago nunca é menor que a compra. Imprima o troco com duas casas e, depois,
quantas notas e moedas de cada valor o caixa entrega, sempre usando a maior que
couber no que falta. Os valores disponíveis, em reais, são

    200  100  50  20  10  5  2  1  0.50  0.25  0.10  0.05  0.01

Mostre só os valores que entram no troco, do maior pro menor, com a quantidade
alinhada à direita em 3 posições, um " x " e o valor alinhado à direita em 6
posições com duas casas. Se o troco for zero, imprima só a primeira linha.

Faça as contas em centavos, com inteiros. Lembra do 0.1 + 0.2 do 013?

Exemplo
    Entrada:
        7.80
        10.00
    Saída:
        troco: 2.20
          1 x   2.00
          2 x   0.10
"""

from iskola import verificar; verificar(__file__)

