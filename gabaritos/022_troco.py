compra = round(float(input()) * 100)
pago = round(float(input()) * 100)

troco = pago - compra
reais, centavos = divmod(troco, 100)
print(f"troco: {reais}.{centavos:02d}")

for valor in (20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1):
    quantidade, troco = divmod(troco, valor)
    if quantidade > 0:
        print(f"{quantidade:>3} x {valor / 100:>6.2f}")
