while True:
    l = int(input())
    if 1 <= l <= 100:
        break
while True:
    c = int(input())
    if 1 <= c <= 100:
        break
l1 = l * c + (l-1) * (c-1)
l2 = ((l-1) + (c-1)) * 2
print(l1, end=f"\n{l2}")