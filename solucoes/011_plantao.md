# Solução do 011 · Plantão

```python
hora, deslocamento = map(int, input().split())

print(f"{(hora + deslocamento) % 24:02d}h")
```

Uma linha só. Somo o deslocamento à hora e tiro o resto por 24, que é o que faz o relógio dar a volta.

O pulo do gato está no negativo. Às 3h, voltar 5 horas dá -2, e -2 % 24 no Python é 22. Em C, Java e JavaScript o mesmo -2 % 24 dá -2, porque lá o resto acompanha o sinal do dividendo. No Python o resto acompanha o sinal do divisor, então com 24 ele sempre fica entre 0 e 23. Por isso não precisa de if nenhum nem de somar 24 antes.

O mesmo vale pra deslocamentos maiores que um dia. 12 + 1000 dá 1012, e 1012 % 24 é 4.

## Complexidade

Tempo O(1) e espaço O(1).
