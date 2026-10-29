# Solução do 013 · Conta do restaurante

Dois problemas se escondem aqui, e cada um derruba uma solução diferente.

O primeiro é o round. Quem escreve round(total) passa em quase tudo e erra o 12.50, que vira 12. O round do Python usa o arredondamento bancário, em que o meio vai pro número par mais próximo. round(0.5) dá 0, round(1.5) dá 2 e round(2.5) dá 2. A ideia é que, somando muitos valores arredondados, os erros pra cima e pra baixo se compensam. A escola manda o meio sempre pra cima, e é isso que o enunciado pede.

O segundo é o float. A soma de 33.66, 79.57 e 14.27 deveria dar 127.50, mas sai 127.49999999999999. Quem troca o round por int(total + 0.5) acerta o 12.50 e erra esse, porque 127.99999999999999 vira 127. O :.2f esconde o problema na primeira linha, já que arredonda pra 127.50 na hora de mostrar, e por isso ele passa despercebido.

## Limpando o float antes

```python
entrada, prato, sobremesa = map(float, input().split())

total = round(entrada + prato + sobremesa, 2)
print(f"Total: {total:.2f}")
print(f"Arredondado: {int(total + 0.5)}")
```

Arredondo o total pra duas casas logo depois de somar. Os preços chegam com centavos, então a soma verdadeira também tem só duas casas, e o round(..., 2) tira o resíduo do binário (aqui o bancário não atrapalha, porque o resíduo é minúsculo e nunca fica no meio entre dois centavos). Depois disso o total + 0.5 é confiável, e o int corta a parte decimal.

## Em centavos

```python
entrada, prato, sobremesa = map(float, input().split())

centavos = round(entrada * 100) + round(prato * 100) + round(sobremesa * 100)
reais, resto = divmod(centavos, 100)
print(f"Total: {reais}.{resto:02d}")
print(f"Arredondado: {(centavos + 50) // 100}")
```

Converto cada preço pra centavos inteiros e não deixo o float participar de mais nenhuma conta. O round aqui só serve pra trocar o 3365.9999999999995 que sai de 33.66 * 100 por 3366. Com inteiros, somar 50 e fazer a divisão inteira por 100 é o arredondamento da escola. O 022 vai por esse caminho.

Pra dinheiro de verdade, o Python tem o módulo decimal, que faz contas em base 10 e deixa escolher a regra de arredondamento. Ele fica pra quando você precisar, mas vale saber que existe.

## Complexidade

Tempo O(1) e espaço O(1).
