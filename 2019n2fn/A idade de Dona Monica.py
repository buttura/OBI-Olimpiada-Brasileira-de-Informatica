l = list()
for _ in range(3):
    while True:
        c = False
        i = int(input())
        if _ == 0:
            if 40 <= i <= 110:
                c = True
                l.append(i)
        if _ == 1:
            if 1 <= i < l[0]:
                c = True
                l.append(i)
        if _ == 2:
            if 1 <= i < l[0] and i != l[1]:
                c = True
                l.append(i)
        if c:
            break
v = l[0] - (l[1] + l[2])
l.append(v)
l.pop(0)
print(max(l))
