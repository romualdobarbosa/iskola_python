# Solução do 007 · Média de duas notas

```python
nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2
print(f"Média: {media:.2f}")
```

O float() faz pelo texto "7.5" o que o int() fazia pelo "17" no 004. Ele também aceita "8" sem casa decimal, então serve pras duas notas.

A barra simples sempre devolve float no Python 3, mesmo quando a conta dá exata. 10 / 2 dá 5.0, e não 5. Quem vem de C ou Java está acostumado com inteiro dividido por inteiro dar inteiro, e no Python isso é o //, que você viu no 006.

O :.2f dentro da f-string diz como mostrar o número. O f é ponto fixo e o .2 são duas casas depois do ponto. Sem ele, a média de 10 e 10 sairia 10.0 e a de 5.1 e 7.3 sairia 6.199999999999999, porque o float guarda os números em binário e às vezes fica um resíduo. O 013 mexe nisso de propósito.

## Complexidade

Tempo O(1) e espaço O(1).
