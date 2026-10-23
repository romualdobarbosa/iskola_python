# Solução do 002 · Lendo a entrada

## Com f-string

```python
nome = input()
print(f"Olá, {nome}!")
```

O input lê uma linha da entrada e devolve uma string sem a quebra de linha do final. A f-string monta a frase colocando o valor de nome onde está {nome}. É o jeito mais comum hoje, e o 003 vai usar bastante.

## Concatenando

```python
nome = input()
print("Olá, " + nome + "!")
```

Também passa. O + junta strings, e o espaço depois da vírgula tem que estar dentro das aspas. Uma armadilha comum é escrever print("Olá,", nome, "!"), que imprime "Olá, Ana !" com um espaço antes da exclamação, porque o print separa cada valor com espaço. O 003 explica isso melhor.

Se você escreveu print("Olá, Ana!") direto, passou no primeiro caso e falhou nos outros três. Pra isso serve ter vários casos.

## Complexidade

Tempo O(n) e espaço O(n), com n o tamanho do nome (ler e copiar a string).
