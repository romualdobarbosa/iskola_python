segundos = int(input())

minutos, segundos = divmod(segundos, 60)
horas, minutos = divmod(minutos, 60)
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
