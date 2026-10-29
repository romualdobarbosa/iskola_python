cidade = input()
populacao = int(input())
area = float(input())

texto_populacao = f"{populacao:_}".replace("_", ".")
texto_densidade = f"{populacao / area:_.2f}".replace(".", ",").replace("_", ".")

print(cidade)
print(f"população: {texto_populacao}")
print(f"densidade: {texto_densidade} hab/km²")
