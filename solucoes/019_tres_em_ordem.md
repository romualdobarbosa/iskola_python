# Solução do 019 · Três em ordem

## Com trocas

```python
a, b, c = map(int, input().split())
em_ordem = a <= b <= c

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
if em_ordem:
    print("já estava em ordem")
else:
    print("fora de ordem")
```

Três comparações com troca colocam três números em ordem. A primeira e a segunda levam o maior pro c. A terceira arruma a e b. É um bubble sort de três elementos, escrito à mão.

O a, b = b, a troca os valores sem variável auxiliar. O Python monta primeiro a tupla do lado direito, com os valores antigos, e só depois atribui. Em C seria preciso um temp.

O detalhe que pega é testar a ordem antes das trocas. Depois delas, a <= b <= c é sempre verdade, e o programa diria "já estava em ordem" pra tudo. Por isso guardei o resultado em em_ordem logo na segunda linha.

## Com min e max

```python
a, b, c = map(int, input().split())

menor = min(a, b, c)
maior = max(a, b, c)
meio = a + b + c - menor - maior

print(menor, meio, maior)
if a <= b <= c:
    print("já estava em ordem")
else:
    print("fora de ordem")
```

O min e o max aceitam vários argumentos e devolvem o menor e o maior. O do meio sai da soma dos três menos os dois das pontas. Aqui os valores originais nunca são alterados, então dá pra testar a ordem no final sem problema.

As duas passam. A das trocas generaliza melhor pra pensar em ordenação, e a do min e max é mais curta. Quando chegar o sorted, no 054, nenhuma das duas vai ser necessária.

## Complexidade

Tempo O(1) e espaço O(1), três números sempre.
