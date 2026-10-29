# Solução do 022 · Troco

```python
compra = round(float(input()) * 100)
pago = round(float(input()) * 100)

troco = pago - compra
reais, centavos = divmod(troco, 100)
print(f"troco: {reais}.{centavos:02d}")

for valor in (20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1):
    quantidade, troco = divmod(troco, valor)
    if quantidade > 0:
        print(f"{quantidade:>3} x {valor / 100:>6.2f}")
```

Converti os dois valores pra centavos logo na leitura, e daí pra frente só tem inteiro. O round aqui não está arredondando dinheiro, só tirando o resíduo do float. 0.57 * 100 dá 56.99999999999999, o int cortaria pra 56 e o round devolve 57. O caso com compra de 0.57 está nos testes por causa disso.

Quem faz a conta em reais e converte no final cai na mesma armadilha com mais força. 10.29 - 10.00 dá 0.28999999999999915, e int(0.28999999999999915 * 100) é 28. O caso com troco de 0.29 também está lá.

A primeira linha usa o divmod do 010 pra separar reais de centavos, e o :02d garante o 0.05 em vez de 0.5.

O for percorre uma tupla com os valores em centavos, do maior pro menor. Em cada volta o divmod diz quantas notas daquele valor cabem e quanto falta, e o que falta vira o troco pra próxima volta. O if pula os valores que não entram. Na hora de imprimir, valor / 100 volta pra reais, e aqui o float não atrapalha porque o :>6.2f arredonda um número que já é quase exato.

## Complexidade

Tempo O(k) e espaço O(1), com k o número de valores de nota e moeda (13, fixo). Na prática, O(1).
