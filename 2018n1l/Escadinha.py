while True:
    q = int(input())
    if 1 <= q <= 1000:
        break
s = 0
while True:
    n = str(input()).split()
    for i in range(len(n)):
        if -10**6 <= int(n[i]) <= 10**6:
            s += 1
    if s == len(n):
        break
    else:
        s = 0
vi = s = 0
l = list()
if len(n) > 1:
    for i in range(len(n)):
        try:
            v = int(n[i]) - int(n[i+1])
            l.append(v)
        except:
            break
    for i in range(len(l)):
        try:
            if l[i] == l[i+1]:
                l.pop(i)
        except:
            break
    for i in range(len(l)):
        try:
            if l[i] == l[i+1]:
                l.pop(i)
        except:
            break
    s = len(l)
else:
    s = 1
print(s)



