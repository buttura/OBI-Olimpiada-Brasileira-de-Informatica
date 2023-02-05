s = 0
b = ["7", "3", "6"]
v = ["1", "5", "8"]
p = ["9", "2", "4"]
while True:
    n = str(input()).split()
    for i in range(len(n)):
        if 1 <= int(n[i]) <= 9:
            s += 1
        else:
            s = 0
    if len(n) == 4 == s:
        break
if (n[0] in b and n[1] in v and n[2] in b and n[3] in p) or (n[0] in v and n[1] in b and n[2] in p and n[3] in b) or (n[0] in b and n[1] in p and n[2] in b and n[3] in v) or (n[0] in p and n[1] in b and n[2] in v and n[3] in b):
    print("V")
else:
    print("F")
