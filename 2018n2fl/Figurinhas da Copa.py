while True:
    v = str(input()).split()
    if 1 <= int(v[0]) <= 100 and 1 <= int(v[1]) <= int(v[0])/2 and 1 <= int(v[2]) <= 300:
        break
s = 0
lfc = list()
while True:
    fc = str(input()).split()
    for i in range(len(fc)):
        if 1 <= int(fc[i]) <= int(v[0]):
            lfc.append(int(fc[i]))
            s += 1
    if s == len(fc):
        break
    else:
        s = 0
s = 0
a = 0
lfcc = list()
while True:
    fcc = str(input()).split()
    for i in range(len(fcc)):
        if 1 <= int(fcc[i]) <= 300:
            if int(fcc[i]) in lfc:
                a += 1
            s += 1
    if s == len(fcc):
        break
    else:
        s = 0
print(len(lfc) - a)

