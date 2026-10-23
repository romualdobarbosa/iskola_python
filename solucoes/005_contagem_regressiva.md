# Solução do 005 · Contagem regressiva

```python
n = int(input())

for i in range(n, 0, -1):
    print(i)
print("Decolar!")
```

O range(início, fim, passo) começa no início, anda de passo em passo e para antes de chegar no fim. Pra contar de n até 1, o fim tem que ser 0, porque o fim nunca entra. É a pegadinha do enunciado. Quem escreve range(n, 1, -1) para no 2.

Com n igual a 0, range(0, 0, -1) é vazio, o for não roda nenhuma vez e só sai o Decolar!. Nenhum if foi necessário pra esse caso.

O for do Python percorre os valores que o range entrega, sem contador manual. Quem vem de C ou Java costuma estranhar no começo e depois não quer mais voltar.

## Complexidade

Tempo O(n), uma volta por número. Espaço O(1), porque o range gera os números conforme o for pede, sem montar uma lista inteira na memória.
