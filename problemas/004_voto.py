"""
004 · Voto

Leia a idade de uma pessoa e diga como é o voto dela no Brasil.

    menos de 16 anos    não vota
    16 ou 17 anos       facultativo
    de 18 a 69 anos     obrigatório
    70 anos ou mais     facultativo

O código abaixo tem um erro clássico de quem vem de outra linguagem. Rode e leia
o Erro de Execução (laranja). O corretor mostra a linha que quebrou e explica o
erro em português. Depois de corrigir, complete o resto das regras.

Vale saber também onde ficam as dicas. Toda falha termina apontando pra
dicas/NNN_nome.md. A dica não traz código, só os termos que valem uma pesquisa
e o link da documentação oficial, pra você chegar lá com as próprias pernas.

Exemplo
    Entrada: 17
    Saída:   facultativo
"""

from iskola import verificar; verificar(__file__)

idade = input()

if idade < 16:
    print("não vota")
