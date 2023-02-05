while True:
    ch = str(input()).split()
    m = int(ch[0])
    n = int(ch[1])
    if 1 <= m <= 10**6 and 2 <= n <= 10**3:
        break
d = dict()
pd = 0
for i in range(int(ch[0])):
    while True:
        c = str(input()).split()
        x = int(c[0])
        v = int(c[1])
        y = int(c[2])
        if 1 <= x <= n and 1 <= y <= n and x != y and 1 <= v <= 10**2:
            pd += v
            if y not in d:
                d[y] = v
            else:
                d[y] += v
            if x not in d:
                d[x] = -v
            else:
                d[x] -= v
            break
s = 0
for v in d.values():
    if v > 0:
        s += v
if s == pd:
    print("N")
else:
    print("S")
print(s)

