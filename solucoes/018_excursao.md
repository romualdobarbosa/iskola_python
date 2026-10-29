# Solução do 018 · Ônibus da excursão

O jeito que vem primeiro na cabeça é math.ceil(alunos / lugares). Ele passa em quase tudo e erra o caso de 100000000000000001 alunos. A barra simples devolve float, e o float tem uns 16 dígitos de precisão. 100000000000000001 vira 1e17 na divisão, o 1 do final some, e o ceil não tem mais como saber que precisava de mais um ônibus.

Os dois jeitos abaixo usam só inteiros e por isso são exatos pra qualquer tamanho.

## Somando antes de dividir

```python
alunos, lugares = map(int, input().split())

onibus = (alunos + lugares - 1) // lugares
print(f"ônibus: {onibus}")
print(f"lugares vazios: {onibus * lugares - alunos}")
```

Somar lugares - 1 antes da divisão inteira faz qualquer resto diferente de zero empurrar o resultado pra cima. Com 45 alunos e 44 lugares, (45 + 43) // 44 dá 2. Com 88, (88 + 43) // 44 dá 2 também, porque não sobrou ninguém.

## Com o sinal trocado

```python
alunos, lugares = map(int, input().split())

onibus = -(-alunos // lugares)
print(f"ônibus: {onibus}")
print(f"lugares vazios: {onibus * lugares - alunos}")
```

O // do Python arredonda pra baixo, na direção de menos infinito, e não na direção do zero como em C. Então -45 // 44 dá -2. Trocando o sinal na entrada e na saída, o arredondamento pra baixo vira pra cima. É a mesma regra que fez o -2 % 24 dar 22 no 011.

Os lugares vazios saem de quantos lugares foram alugados menos quantos alunos sentaram.

## Complexidade

Tempo O(1) e espaço O(1).
