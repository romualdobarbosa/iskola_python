import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1
print(f"distância: {math.hypot(dx, dy):.2f}")
print(f"metros inteiros: {math.isqrt(dx * dx + dy * dy)}")
