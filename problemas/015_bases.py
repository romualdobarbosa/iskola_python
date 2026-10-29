"""
015 · Painel binário

O painel da oficina mostra um número de 0 a 255 em quatro bases. Leia a base em
que o número foi escrito (2, 8, 10 ou 16) e o número, na mesma linha, e imprima
o valor em decimal, binário, octal e hexadecimal.

O binário aparece nas 8 lâmpadas do painel, então sai sempre com 8 dígitos,
completando com zero à esquerda. O hexadecimal sai em maiúsculas e com 2
dígitos. O octal e o decimal saem sem zero à esquerda. Na entrada, o
hexadecimal pode vir em maiúsculas ou minúsculas.

Exemplo
    Entrada: 2 1011
    Saída:
        decimal: 11
        binário: 00001011
        octal: 13
        hexadecimal: 0B
"""

from iskola import verificar; verificar(__file__)

