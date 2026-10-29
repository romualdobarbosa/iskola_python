# Solução do 010 · Relógio digital

```python
segundos = int(input())

minutos, segundos = divmod(segundos, 60)
horas, minutos = divmod(minutos, 60)
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
```

O primeiro divmod separa os segundos em minutos completos e segundos que sobram. O segundo pega esses minutos e separa em horas e minutos. Reaproveitei os nomes segundos e minutos pros restos, porque depois de cada linha é isso que eles passam a ser.

O :02d é a novidade. O d é inteiro em decimal, o 2 é a largura mínima e o 0 diz pra completar com zero em vez de espaço. Sem ele, 3661 sairia 1:1:1.

Como as horas não passam de 99, a largura 2 sempre basta. Se passasse, o Python não cortaria o número, só deixaria de completar.

## Complexidade

Tempo O(1) e espaço O(1).
