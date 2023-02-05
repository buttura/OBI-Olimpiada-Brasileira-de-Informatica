while True:
    l = int(input())
    if 1 <= l <= 1000:
        break
while True:
    c = int(input())
    if 1 <= c <= 1000:
        break
if l % 2 == 0 and c % 2 != 0 or l % 2 != 0 and c % 2 == 0:
    print(0)
elif l % 2 == 0 and c % 2 == 0 or l % 2 != 0 and c % 2 != 0:
    print(1)
