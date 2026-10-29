"""
014 · Ano bissexto

Leia um ano e diga se ele é bissexto ou comum. A regra do calendário é esta:

    divisível por 4 é bissexto,
    a não ser que seja divisível por 100,
    a não ser que seja divisível por 400, aí volta a ser bissexto.

Então 2024 é bissexto, 1900 é comum e 2000 é bissexto. Tente escrever a regra
toda numa expressão só, juntando as condições com and, or e not.

Exemplo
    Entrada: 1900
    Saída:   comum
"""

from iskola import verificar; verificar(__file__)

