total, tamanho = map(int, input().split())

pacotes, soltas = divmod(total, tamanho)
print(f"pacotes: {pacotes}")
print(f"soltas: {soltas}")
