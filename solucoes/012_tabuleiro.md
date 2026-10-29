# Solução do 012 · Grãos no tabuleiro

## Com a fórmula

```python
n = int(input())

print(f"casa: {2 ** (n - 1)}")
print(f"total: {2**n - 1}")
```

A casa n tem 2 ** (n - 1) grãos. O total da casa 1 até a n é 1 + 2 + 4 + ... + 2 ** (n - 1), e essa soma é sempre uma potência de 2 menos 1. Dá pra ver nos primeiros totais, 1, 3, 7, 15, 31. É a soma de uma progressão geométrica, e em binário fica mais óbvio ainda (somar 1, 10, 100 e 1000 dá 1111, que é 10000 menos 1).

## Somando

```python
n = int(input())

casa = 1
total = 1
for _ in range(n - 1):
    casa *= 2
    total += casa

print(f"casa: {casa}")
print(f"total: {total}")
```

Também passa. Começo com a casa 1 e, a cada volta, dobro a casa e somo no total. Quem não lembra da fórmula chega aqui, e com n até 200 o laço é instantâneo.

## Inteiros sem limite

A casa 64 tem 9223372036854775808 grãos, que é 2 elevado a 63. Num long do Java, que é um inteiro de 64 bits com sinal, esse número já não cabe, e o total da casa 64 só caberia num inteiro sem sinal. No Python o int cresce o quanto a memória deixar, e a casa 200 sai com 60 dígitos sem nenhum cuidado extra. O preço é que contas com inteiros gigantes ficam mais lentas, mas aqui isso nem aparece.

## Complexidade

Com a fórmula, a potência faz O(log n) multiplicações. Somando, são n voltas. Nos dois casos as contas com números gigantes custam proporcional ao número de dígitos, o que com n até 200 não pesa. Espaço O(n) bits pra guardar o número, porque 2 ** n tem n + 1 dígitos binários.
