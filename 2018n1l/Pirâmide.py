while True:
    n = int(input())
    if 1 <= n <= 100:
        break
for i in range(n):
    c = 0
    while True:
        s = str(input()).split()
        for x in range(len(s)):
            if 1 <= int(s[x]) <= 100:
                c += 1
        if c == n:
            break
        else:
            c = 0
