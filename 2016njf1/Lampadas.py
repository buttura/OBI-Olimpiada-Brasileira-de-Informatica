while True:
    n = int(input())
    if 1 <= n <= 10**5:
        break
s = 0
while True:
    f = str(input()).split()
    for i in range(len(f)):
        if 1 <= int(f[i]) <= 2:
            s += 1
    if n == s == len(f):
        break
d = {"A": 0, "B": 0}
for i in range(len(f)):
    if f[i] == "2":
        if d["A"] == 0:
            d["A"] = 1
        else:
            d["A"] = 0
        if d["B"] == 0:
            d["B"] = 1
        else:
            d["B"] = 0
    else:
        if d["A"] == 0:
            d["A"] = 1
        else:
            d["A"] = 0
for v in d.values():
    print(v)