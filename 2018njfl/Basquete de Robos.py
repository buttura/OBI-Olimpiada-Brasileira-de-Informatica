while True:
    d = float(input())
    if 0 <= d <= 2000:
        break
s = 1
if d >= 800:
    s += 1
if d > 1400:
    s += 1
print(s)
