# Solução do 017 · Ponto de ônibus

```python
import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1
print(f"distância: {math.hypot(dx, dy):.2f}")
print(f"metros inteiros: {math.isqrt(dx * dx + dy * dy)}")
```

O import math traz o módulo pra dentro do programa, e as funções dele ficam em math.alguma_coisa. Pra distância usei math.hypot(dx, dy), que é a raiz de dx² + dy², o Pitágoras pronto. math.sqrt(dx * dx + dy * dy) também passa, e math.dist((x1, y1), (x2, y2)) faz a conta inteira recebendo os dois pontos.

Pros metros inteiros, o caminho óbvio é int(math.hypot(dx, dy)). Ele passa em todos os casos, menos no último. Com dx igual a 800000000 e dy igual a 40000, a distância verdadeira é 800000000.9999999994, só que o float não tem dígitos suficientes pra guardar isso e arredonda pra 800000001.0. O int devolve 800000001, que é um metro a mais.

O math.isqrt(n) calcula a parte inteira da raiz de um inteiro sem passar por float, então é sempre exato. Como as coordenadas são inteiras, dx * dx + dy * dy também é, e o isqrt dá a resposta certa. O 032 usa ele de novo.

A primeira linha não sofre com isso. 800000000.9999999994 com duas casas é 800000001.00 de qualquer jeito.

## Complexidade

Tempo O(1) e espaço O(1). Com números gigantes de verdade, o isqrt custa proporcional ao número de dígitos, mas aqui são no máximo 19.
