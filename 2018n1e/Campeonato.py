s = 0
p = ""

l = list()
ofi = list()
li = list()
of = list()

while True:
    n = str(input()).split()
    for i in range(len(n)):
        if 1 <= int(n[i]) <= 16:
            s += 1
        if n[i] not in l:
            l.append(n[i])
            s += 1
    if s == 32:
        break
    else:
        s = 0
        l.clear()
for i in range(len(n)):
    li.append(n[i])
    if i % 2 != 0:
        of.append(li[:])
        li.clear()
a = True
if a:
    for i in range(len(of)):
        for x in range(len(of[i])):
            if "1" in of[i] and "9" in of[i]:
                p = "oitavas"
                a = False
                break
if a:
    for i in range(len(of)):
        for x in range(len(of[i])):
            if of[i][x] == "1" or of[i][x] == "9":
                if x == 0:
                    of[i].pop(1)
                    break
                else:
                    of[i].pop(0)
                    break
            else:
                of[i].pop(0)
                break
    li.clear()
    for i in range(len(of)):
        li.append(of[i][0])
    of.clear()
    for i in range(len(li)):
        of.append(li[i])
        if i % 2 != 0:
            ofi.append(of[:])
            of.clear()
    for i in range(len(ofi)):
        for x in range(len(ofi[i])):
            if "1" in ofi[i] and "9" in ofi[i]:
                p = "quartas"
                a = False
                break
if a:
    for i in range(len(ofi)):
        for x in range(len(ofi[i])):
            if ofi[i][x] == "1" or ofi[i][x] == "9":
                if x == 0:
                    ofi[i].pop(1)
                    break
                else:
                    ofi[i].pop(0)
                    break
            else:
                ofi[i].pop(0)
                break
    li.clear()
    for i in range(len(ofi)):
        li.append(ofi[i][0])
    of.clear()
    ofi.clear()
    for i in range(len(li)):
        of.append(li[i])
        if i % 2 != 0:
            ofi.append(of[:])
            of.clear()
    for i in range(len(ofi)):
        for x in range(len(ofi[i])):
            if "9" in ofi[i] and "1" in ofi[i]:
                p = "semifinal"
                a = False
                break
if a:
    p = "final"
print(p)
