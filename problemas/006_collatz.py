"""
006 · Collatz

Leia um inteiro positivo n e conte quantos passos ele leva pra chegar a 1
seguindo a regra abaixo.

    se n é par,    n vira n dividido por 2
    se n é ímpar,  n vira 3 vezes n mais 1

Com n = 6 o caminho é 6, 3, 10, 5, 16, 8, 4, 2, 1. São 8 passos.

O código abaixo não termina pra quase nenhuma entrada. Quando isso acontece, o
corretor corta em 2 segundos e dá Tempo Limite Excedido (magenta). Descubra por
que o laço não para.

Este é o último tutorial. Quando passar, abra solucoes/006_collatz.md. As
soluções ficam numa pasta separada de propósito, pra dar trabalho ir olhar antes
da hora. Depois do Aceito é a melhor hora de ler, porque você compara o seu
jeito com outro e quase sempre aprende alguma coisa.

Exemplo
    Entrada: 6
    Saída:   8
"""

from iskola import verificar; verificar(__file__)

n = int(input())
passos = 0

while n != 1:
    if n % 2 == 0:
        n // 2
    else:
        n = 3 * n + 1
    passos += 1

print(passos)
