alunos, lugares = map(int, input().split())

onibus = -(-alunos // lugares)
print(f"ônibus: {onibus}")
print(f"lugares vazios: {onibus * lugares - alunos}")
