entrada, prato, sobremesa = map(float, input().split())

centavos = round(entrada * 100) + round(prato * 100) + round(sobremesa * 100)
reais, resto = divmod(centavos, 100)
print(f"Total: {reais}.{resto:02d}")
print(f"Arredondado: {(centavos + 50) // 100}")
