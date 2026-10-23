# Solução do 006 · Collatz

```python
n = int(input())
passos = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    passos += 1

print(passos)
```

No template, a linha n // 2 calculava a metade e jogava o resultado fora. O n nunca mudava quando era par, então o laço girava pra sempre. A correção é n //= 2, que é o mesmo que n = n // 2.

Usei // e não /. A barra simples sempre devolve float, e 6 / 2 dá 3.0. Nesse problema até funcionaria, mas os números crescem bastante (o 27 passa de 9 mil no caminho) e com float grande você começa a perder precisão. Com // o n continua inteiro.

O % devolve o resto da divisão, então n % 2 == 0 diz se o número é par.

## Complexidade

Aqui a coisa fica curiosa. Ninguém sabe se esse laço termina pra todo n. É a conjectura de Collatz, testada por computador pra números enormes e nunca provada. Então a gente não tem um Big-O de tempo pra dar, só a contagem de passos de cada caso (111 pro 27). Espaço O(1), só duas variáveis.

Você já passou pelos 6 tutoriais. Daqui pra frente cada problema traz só o enunciado e a área em branco, e a solução de cada um mora aqui em solucoes/.
