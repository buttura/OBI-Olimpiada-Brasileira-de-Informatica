l = list()
for i in range(4):
    while True:
        n = int(input())
        if 1 <= n <= 100:
            l.append(n)
            break
if l[0] * l[1] > l[2] * l[3]:
    print(l[0] * l[1])
else:
    print(l[2] * l[3])
