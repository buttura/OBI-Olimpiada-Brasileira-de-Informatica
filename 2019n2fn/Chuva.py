s = str(input()).split()
x = int(s[0])
y = int(s[1])

interface = str(input())
ltemp = list()
m = list()
a = ""
for i in range(len(interface)):
    if i % y == 0 and i != 0:
        a += "\n"
    else:
        a += interface[i]
print(a)
