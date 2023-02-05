s = 0
while True:
    f = str(input()).split()
    for i in range(len(f)):
        if 1 <= int(f[i]) <= 1000:
            s += 1
    if s == len(f) == 2:
        break
    else:
        s = 0
s = 0
l = list()
for i in range(int(f[0])):
    while True:
        v = str(input()).split()
        for x in range(len(v)):
            if 0 <= int(v[x]) <= 3:
                s += 1
        if s == len(v) == int(f[1]):
            l.append(v[:])
            break
        else:
            s = 0
    s = 0
c = False
y = x = 0
for ini in range(len(l)):
    for fin in range(len(l[ini])):
        if l[ini][fin] == "2":
            p = l[ini][fin]
            y = ini
            x = fin
while True:
    if y != len(l)-1:
        if l[y+1][x] == "1":
            s += 1
            l[y+1][x] = "2"
            y += 1
        elif l[y+1][x] == "3":
            c = True
    if y != 0:
        if l[y-1][x] == "1":
            s += 1
            l[y-1][x] = "2"
            y -= 1
        elif l[y-1][x] == "3":
            c = True
    if x != len(l[0])-1:
        if l[y][x+1] == "1":
            s += 1
            l[y][x+1] = "2"
            x += 1
        elif l[y][x+1] == "3":
            c = True
    if x != 0:
        if l[y][x-1] == "1":
            s += 1
            l[y][x-1] = "2"
            x -= 1
        elif l[y][x-1] == "3":
            c = True
    if c:
        break
# 4 5
# 0 1 1 1 0
# 0 2 0 1 1
# 0 0 0 0 1
# 3 1 1 1 1
print(s+2)
