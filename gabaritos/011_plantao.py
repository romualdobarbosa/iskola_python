hora, deslocamento = map(int, input().split())

print(f"{(hora + deslocamento) % 24:02d}h")
