a, b, c = map(int, input().split())
em_ordem = a <= b <= c

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
if em_ordem:
    print("já estava em ordem")
else:
    print("fora de ordem")
