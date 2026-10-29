ano = int(input())

bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if bissexto:
    print("bissexto")
else:
    print("comum")
