# Solução do 021 · Censo

```python
cidade = input()
populacao = int(input())
area = float(input())

texto_populacao = f"{populacao:_}".replace("_", ".")
texto_densidade = f"{populacao / area:_.2f}".replace(".", ",").replace("_", ".")

print(cidade)
print(f"população: {texto_populacao}")
print(f"densidade: {texto_densidade} hab/km²")
```

A opção de agrupamento da especificação de formato aceita vírgula ou sublinhado. O :, daria "1,234,567", e o :_ dá "1_234_567". Escolhi o sublinhado de propósito.

Pra população basta trocar o _ por ponto. Pra densidade, f"{x:_.2f}" dá "1_460.82", e são duas trocas. Primeiro o ponto decimal vira vírgula, depois o sublinhado vira ponto. Se tivesse usado :, no lugar de :_, as duas trocas iam brigar, porque trocar a vírgula por ponto e depois o ponto por vírgula desfaz tudo, e aí precisaria de um caractere temporário no meio. Com o sublinhado nenhum caractere aparece nos dois papéis, e basta cuidar da ordem. Se o sublinhado virar ponto primeiro, a troca seguinte transforma todos os pontos em vírgula.

O Python tem o módulo locale, que formata no padrão do país configurado no sistema. Mas o resultado depende da máquina onde o código roda, e num corretor (ou num servidor) isso costuma dar dor de cabeça. A troca manual dá o mesmo resultado em qualquer lugar.

## Complexidade

Tempo O(d) e espaço O(d), com d o número de dígitos, por causa das strings montadas na formatação. Na prática, O(1).
