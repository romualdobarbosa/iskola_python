# Solução do 003 · Crachá

O template fazia print(sobrenome + ", ", nome). O print recebe dois valores e põe um espaço entre eles, e a string já terminava com espaço. Resultado, "Silva,  Ana" com dois espaços. A resposta estava certa e a formatação não, por isso Erro de Apresentação.

## Com f-string

```python
nome = input()
sobrenome = input()
dia = input()
mes = input()
ano = input()

print(f"{sobrenome}, {nome}")
print(f"{dia}/{mes}/{ano}")
```

Com f-string você escreve a linha do jeito que ela tem que sair, e o que está entre chaves vira o valor da variável. Não tem separador escondido.

## Com sep e end

```python
nome = input()
sobrenome = input()
dia = input()
mes = input()
ano = input()

print(sobrenome, end=", ")
print(nome)
print(dia, mes, ano, sep="/")
```

O sep troca o que vai entre os valores (o padrão é um espaço) e o end troca o que vai no fim (o padrão é a quebra de linha). Aqui o primeiro print termina com ", " em vez de quebrar a linha, e o nome sai logo depois. Pra data, sep="/" resolve sem montar string nenhuma.

Os dois passam. No dia a dia a f-string ganha na maioria das vezes, mas sep e end aparecem bastante quando você imprime uma lista de valores.

## Complexidade

Tempo O(n) e espaço O(n), com n o tamanho total da entrada.
