# Solução do 016 · Quantos positivos

```python
a, b, c, d = map(int, input().split())

positivos = (a > 0) + (b > 0) + (c > 0) + (d > 0)
dois_digitos = (10 <= a <= 99) + (10 <= b <= 99) + (10 <= c <= 99) + (10 <= d <= 99)

print(f"positivos: {positivos}")
print(f"dois dígitos: {dois_digitos}")
```

No Python, bool é subclasse de int. True vale 1 e False vale 0, e dá pra somar comparações direto. (a > 0) + (b > 0) conta quantas deram True. Os parênteses são obrigatórios, porque o + tem precedência maior que o >.

O 10 <= a <= 99 é a comparação encadeada. O Python lê como 10 <= a and a <= 99, mas sem repetir o a. Em C, a mesma linha compararia 10 <= a, que dá 0 ou 1, com 99, e daria sempre verdadeiro.

Com quatro variáveis a linha fica comprida. Quando chegar nas listas, a mesma ideia vira uma linha curta com sum, e o 024 faz a contagem com laço.

## Complexidade

Tempo O(1) e espaço O(1).
