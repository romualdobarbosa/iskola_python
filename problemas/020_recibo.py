"""
020 · Recibo

Leia a quantidade N de itens da compra e, nas N linhas seguintes, o produto, a
quantidade e o preço unitário, separados por espaço. O nome do produto é uma
palavra só, com até 12 letras.

Pra cada item imprima uma linha do recibo com três colunas:

    o produto alinhado à esquerda, ocupando 12 posições
    a quantidade alinhada à direita, ocupando 4 posições
    o valor do item (quantidade vezes preço) alinhado à direita, ocupando
    10 posições, com duas casas decimais

Se errar uma coluna, o Erro de Apresentação mostra cada espaço como ·, então
dá pra contar.

Exemplo
    Entrada:
        2
        pão 6 0.75
        leite 2 4.99
    Saída:
        pão            6      4.50
        leite          2      9.98
"""

from iskola import verificar; verificar(__file__)

