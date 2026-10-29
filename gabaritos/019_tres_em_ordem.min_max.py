a, b, c = map(int, input().split())

menor = min(a, b, c)
maior = max(a, b, c)
meio = a + b + c - menor - maior

print(menor, meio, maior)
if a <= b <= c:
    print("já estava em ordem")
else:
    print("fora de ordem")
