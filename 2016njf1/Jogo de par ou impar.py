while True:
    p = int(input())
    if p == 1 or p == 0:
        break
while True:
    d_1 = int(input())
    if 0 <= d_1 <= 5:
        break
while True:
    d_2 = int(input())
    if 0 <= d_2 <= 5:
        break
if p == 0 and (d_1 + d_2) % 2 == 0:
    print(0)
elif p == 1 and (d_1 + d_2) % 2 == 0:
    print(1)
elif p == 0 and (d_1 + d_2) % 2 != 0:
    print(1)
else:
    print(0)