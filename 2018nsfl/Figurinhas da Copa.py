while True:
    s = str(input()).split()
    if len(s) == 3 and 1 <= int(s[0]) <= 100 and 1 <= int(s[1]) <= int(s[0])/2 and 1 <= int(s[2]) <= 300:
        break
c = 0
lfc = list()
while True:
    f = str(input()).split()
    for i in range(len(f)):
        if 1 <= int(f[i]) <= int(s[0]):
            lfc.append(int(f[i]))
            c += 1
    if c == len(f):
        break
    else:
        c = 0
        lfc.clear()
c = 0
lf = list()
while True:
    fc = str(input()).split()
    for i in range(len(fc)):
        if 1 <= int(fc[i]) <= 300:
            lf.append(int(fc[i]))
            c += 1
    if c == len(fc):
        break
    else:
        c = 0
        lf.clear()
a = 0
for i in range(len(lf)):
    if lf[i] in lfc:
        a += 1
print(len(lfc) - a)
