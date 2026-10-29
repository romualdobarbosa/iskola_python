n = int(input())

casa = 1
total = 1
for _ in range(n - 1):
    casa *= 2
    total += casa

print(f"casa: {casa}")
print(f"total: {total}")
