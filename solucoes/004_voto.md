# Solução do 004 · Voto

```python
idade = int(input())

if idade < 16:
    print("não vota")
elif idade < 18 or idade >= 70:
    print("facultativo")
else:
    print("obrigatório")
```

O erro do template era comparar o que veio do input direto com 16. O input sempre devolve string, e o Python não compara string com número (em JavaScript, por exemplo, "17" < 16 funciona e dá false, o Python prefere quebrar). O int() converte o texto pra inteiro antes de qualquer conta.

A ordem das condições faz parte da solução. Quando o primeiro if falha, já se sabe que a idade é pelo menos 16, então o elif só precisa olhar o "menos de 18" e o "70 ou mais". O que sobra cai no else.

Daria pra escrever as faixas por extenso, como 16 <= idade <= 17. O Python aceita comparação encadeada assim, coisa que muita linguagem não aceita, e às vezes ela deixa a regra mais legível. Aqui a ordem do if já garante os limites.

## Complexidade

Tempo O(1) e espaço O(1).
