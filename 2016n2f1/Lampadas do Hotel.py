lista = list()
s = 0
while True:
    l = str(input()).split()
    for i in range(len(l)):
        if 0 <= int(l[i]) <= 1:
            lista.append(int(l[i]))
            s += 1
    if s == len(l):
        break
    else:
        s = 0
        lista.clear()
s = 0
if lista[0] != lista[2] and lista[1] != lista[3] or lista[0] != lista[2] and lista[1] == lista[3]:
    s = 1
elif lista[0] == lista[2] and lista[1] != lista[3]:
    s = 2
print(s)
