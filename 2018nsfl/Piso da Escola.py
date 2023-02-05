while True:
    l = int(input())
    if 1 <= l <= 100:
        break
while True:
    c = int(input())
    if 1 <= c <= 100:
        break
p1 = l * c + (l-1) * (c-1)
p2 = ((l-1) + (c-1)) * 2
print(p1)
print(p2)
