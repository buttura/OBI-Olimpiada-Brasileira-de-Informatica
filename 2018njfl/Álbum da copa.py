while True:
    n = int(input())
    if 1 <= n <= 100:
        break
while True:
    m = int(input())
    if 1 <= m <= 300:
        break
l = list()
for i in range(m):
    while True:
        v = int(input())
        if 1 <= v <= n:
            break
    if v not in l:
        l.append(v)
print(n - len(l))