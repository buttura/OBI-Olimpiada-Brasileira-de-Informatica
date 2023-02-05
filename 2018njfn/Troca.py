q = str(input()).split()
while True:
    s = 0
    cima = str(input()).split()
    baixo = str(input()).split()
    for i in range(int(q[0])):
        if 1 <= int(cima[i]) <= 10**5 and 1 <= int(baixo[i]) <= 10**5:
            s += 1
    if len(cima) == int(q[0]) == len(baixo) and s == int(q[0]):
        break
    else:
        s = 0
for i in range(int(q[1])):
    while True:
        t = str(input()).split()
        if 1 <= int(t[0]) <= 10**5 and 1 <= int(t[1]) <= 10**5:
            break
    for x in range(int(t[0])-1, int(t[1])):
        b = baixo[x]
        c = cima[x]
        cima[x] = b
        baixo[x] = c
for i in range(len(cima)):
    print(int(cima[i]), end=" ")

# 16 1
# 31 2 45 3 8 1 32 10 4 27 12 7 7 9 63 47
# 1 12 6 4 97 2 87 10 3 9 55 56 11 90 3 8
# 5 11

# 10 5
# 7 88 23 44 1 67 73 2 9 11
# 4 55 1 1 3 74 82 9 8 37
# 1 3
# 5 10
# 2 6
# 5 9
# 1 7
