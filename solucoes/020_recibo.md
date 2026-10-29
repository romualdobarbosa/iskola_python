# Solução do 020 · Recibo

```python
n = int(input())

for _ in range(n):
    produto, quantidade, preco = input().split()
    quantidade = int(quantidade)
    valor = quantidade * float(preco)
    print(f"{produto:<12}{quantidade:>4}{valor:>10.2f}")
```

O for com range(n) roda uma vez por item, e o _ é a convenção pra variável que a gente não vai usar. Cada linha vem com três pedaços de tipos diferentes, então desempacotei como texto e converti um por um. O map do 008 não serve aqui, porque ele aplica a mesma função em todos.

O formato tem três partes. O :<12 alinha o produto à esquerda em 12 posições, completando com espaço. O :>4 alinha a quantidade à direita em 4. O :>10.2f junta o alinhamento com as duas casas do 007 e alinha o valor à direita em 10 posições. Como cada coluna tem largura fixa, os números ficam um embaixo do outro, independente do tamanho do nome.

Pra string o padrão já é alinhar à esquerda, e pra número é alinhar à direita. Então :12 e :4 também funcionariam, mas deixar o sinal escrito ajuda quem lê.

## Complexidade

Tempo O(n) e espaço O(1), com n o número de itens. Cada linha é impressa logo depois de lida, sem guardar nada.
