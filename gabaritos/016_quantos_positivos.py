a, b, c, d = map(int, input().split())

positivos = (a > 0) + (b > 0) + (c > 0) + (d > 0)
dois_digitos = (10 <= a <= 99) + (10 <= b <= 99) + (10 <= c <= 99) + (10 <= d <= 99)

print(f"positivos: {positivos}")
print(f"dois dígitos: {dois_digitos}")
