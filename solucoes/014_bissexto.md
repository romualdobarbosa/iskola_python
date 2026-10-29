# Solução do 014 · Ano bissexto

```python
ano = int(input())

bissexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if bissexto:
    print("bissexto")
else:
    print("comum")
```

A regra com "a não ser que" fica mais fácil reescrita assim. Um ano é bissexto se é divisível por 4 e não por 100, ou se é divisível por 400. Traduzindo palavra por palavra sai a expressão da terceira linha.

Não coloquei parênteses porque o and tem precedência maior que o or, igual multiplicação e soma. O Python lê como (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0. Quem preferir pode escrever os parênteses, eles não mudam nada e deixam a intenção à mostra.

Guardar o resultado numa variável com nome ajuda a ler o if depois. A expressão booleana é um valor como qualquer outro, e dá pra guardar, imprimir e passar adiante.

Outra forma que passa é a cadeia de if e elif, testando 400, depois 100, depois 4. A ordem importa, e testar o 4 primeiro erra o 1900. A biblioteca padrão tem calendar.isleap, que faz exatamente isso, mas aí o exercício perde a graça.

## Complexidade

Tempo O(1) e espaço O(1).
