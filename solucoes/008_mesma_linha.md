# Solução do 008 · Dois na mesma linha

## Com map

```python
a, b = map(int, input().split())

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
```

O input() devolve "3 5" e o split() quebra nos espaços, devolvendo ["3", "5"]. Sem argumento, o split trata qualquer quantidade de espaços como um separador só, por isso o caso "12   30" passa. Com split(" ") ele cortaria em cada espaço e sobrariam strings vazias no meio.

O map(int, ...) aplica o int em cada pedaço. E o a, b = ... é o desempacotamento, que pega o primeiro valor pra a e o segundo pra b. Se a linha tivesse três números, daria erro, e isso é bom (é melhor quebrar do que seguir com dado errado).

## Sem map

```python
a, b = input().split()
a = int(a)
b = int(b)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
```

Também passa, e deixa claro que os pedaços chegam como texto. Com dois valores tanto faz. Quando forem cinco, o map economiza bastante linha.

Repare no -8 + -3 = -11 de um dos casos. A f-string só coloca o valor onde está a chave e não tenta embelezar a conta, e o enunciado pede exatamente isso.

## Complexidade

Tempo O(n) e espaço O(n), com n o tamanho da linha (o split monta a lista de pedaços).
