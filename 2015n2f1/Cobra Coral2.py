c = s = 0
while True:
    n = str(input()).split()
    for i in range(len(n)):
        if 1 <= int(n[i]) <= 9:
            s += int(n[i])
            c += 1
        else:
            c = 0
    if c == len(n) == 4:
        break
if s % 2 == 0:
    print("V")
else:
    print("F")
