while True:
    s = int(input())
    if 0 <= s <= 5000:
        break
c = 0
while True:
    n = str(input()).split()
    for i in range(len(n)):
        if int(n[i]) <= 500:
            c += 1
    if c == len(n) == 6:
        break
    else:
        c = 0
c = 0
