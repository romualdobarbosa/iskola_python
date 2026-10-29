n = int(input())

for _ in range(n):
    produto, quantidade, preco = input().split()
    quantidade = int(quantidade)
    valor = quantidade * float(preco)
    print(f"{produto:<12}{quantidade:>4}{valor:>10.2f}")
