t = str(input()).split()
while True:
    n = str(input()).split()
    if len(n) == int(t[0]):
        break
tot = s = 0
for i in range(int(t[0])):
    s += int(n[i])
    if s > int(t[1]):
        s = 0
    if i >= 1:
        if int(n[i-1]) != int(n[i]) and int(n[i]) == int(t[1]):
            tot -= 1
            print(tot, i, "Tirei Um!")
    if int(n[i]) == int(t[1]):
        tot += 1
        print(tot, i, "Valor Igual")
    if s == int(t[1]):
        tot += 1
        print(tot, i, "Soma Igual")
print(tot)
