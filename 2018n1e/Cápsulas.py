while True:
    n = str(input()).split()
    if len(n) == 2:
        break
while True:
    f = str(input()).split()
    if 1 <= len(f) <= int(n[0]):
        break
d = c = 0
while d < int(n[1]):
    c += 1
    for i in range(int(n[0])):
        if c % int(f[i]) == 0:
            d += 1
print(c)