alunos, lugares = map(int, input().split())

onibus = (alunos + lugares - 1) // lugares
print(f"ônibus: {onibus}")
print(f"lugares vazios: {onibus * lugares - alunos}")
