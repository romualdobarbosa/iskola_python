# Solução do 009 · Pacotes de figurinhas

## Com divmod

```python
total, tamanho = map(int, input().split())

pacotes, soltas = divmod(total, tamanho)
print(f"pacotes: {pacotes}")
print(f"soltas: {soltas}")
```

O divmod(n, p) devolve o quociente e o resto juntos, e o desempacotamento do 008 separa os dois numa linha só. É a cara do problema, uma divisão com duas respostas.

## Com // e %

```python
total, tamanho = map(int, input().split())

print(f"pacotes: {total // tamanho}")
print(f"soltas: {total % tamanho}")
```

Mesmo resultado, com os dois operadores que apareceram no 006. O // é a divisão inteira, e o % é o resto. O divmod faz as duas contas de uma vez e por isso aparece muito quando você precisa das duas, como no 010.

N igual a 0 dá 0 pacotes e 0 soltas sem nenhum caso especial, e N menor que P dá 0 pacotes e N soltas.

## Complexidade

Tempo O(1) e espaço O(1).
