total, tamanho = map(int, input().split())

print(f"pacotes: {total // tamanho}")
print(f"soltas: {total % tamanho}")
