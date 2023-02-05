l = list()
for _ in range(4):
    while True:
        v = int(input())
        if 1 <= v <= 100:
            l.append(v)
            break
if l[1] == l[3] and l[0] > l[2] or l[1] > l[2] and l[0] == l[3] or l[0] > l[3] and l[1] == l[2]:
    print(1)
elif l[1] == l[3] and l[2] > l[1] or l[1] < l[2] and l[0] == l[3] or l[0] < l[3] and l[1] == l[2]:
    print(2)
else:
    print(-1)
