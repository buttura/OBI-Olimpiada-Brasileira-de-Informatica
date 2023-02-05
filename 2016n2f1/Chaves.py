while True:
    n = int(input())
    if 1 <= n <= 10**3:
        break
e = 0
for i in range(n):
    while True:
        f = str(input())
        if 0 <= len(f) <= 100:
            break
    for x in range(len(f)):
        if f[x] == "{":
            e += 1
        elif f[x] == "}":
            e -= 1
if e == 0:
    print("S")
else:
    print("N")
