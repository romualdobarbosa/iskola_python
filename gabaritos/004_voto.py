idade = int(input())

if idade < 16:
    print("não vota")
elif idade < 18 or idade >= 70:
    print("facultativo")
else:
    print("obrigatório")
