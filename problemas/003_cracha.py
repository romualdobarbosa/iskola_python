"""
003 · Crachá

Leia nome, sobrenome, dia, mês e ano de nascimento, um por linha, e imprima o
crachá no formato do exemplo. Dia e mês sempre chegam com dois dígitos.

O código abaixo quase resolve, mas sobra espaço. Quando a resposta está certa e
só a formatação erra, o corretor dá Erro de Apresentação (amarelo) e mostra cada
espaço como · e cada quebra de linha como ⏎. Dá pra resolver com f-string ou com
os parâmetros sep e end do print. Vale testar os dois.

Exemplo
    Entrada:
        Ana
        Silva
        07
        03
        1994
    Saída:
        Silva, Ana
        07/03/1994
"""

from iskola import verificar; verificar(__file__)

nome = input()
sobrenome = input()
dia = input()
mes = input()
ano = input()

print(sobrenome + ", ", nome)
print(dia, mes, ano, sep="/")
