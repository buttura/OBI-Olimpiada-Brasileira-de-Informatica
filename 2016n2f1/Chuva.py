while True:
    n = int(input())
    if 1 <= n <= 10**5:
        break
l = list()
for i in range(n):
    while True:
        h = int(input())
        if 1 <= h <= 10**9:
            l.append(h)
            break
s = 0

lr = l[:]
lr.reverse()

if lr[0] < l[0]:
    s -= 1
for i in range(1, len(lr)):
    if lr[i] == lr[0] and lr[0] != l[0]:
        s -= 1
    elif lr[i] > l[0]:
        break
ap = l[0]
while len(l) > 0:
    if l[0] < ap:
        s += 1
    l.pop(0)
print(s)
