entrada, prato, sobremesa = map(float, input().split())

total = round(entrada + prato + sobremesa, 2)
print(f"Total: {total:.2f}")
print(f"Arredondado: {int(total + 0.5)}")
