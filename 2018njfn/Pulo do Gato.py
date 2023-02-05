while True:
    n = int(input())
    if 1 <= n <= 10**4:
        break
while True:
    pb = str(input()).split()
    if len(pb) == n and pb[0] == "1" == pb[len(pb)-1]:
        break
certo = True
s = tot = 0
for i in range(len(pb)):
    if i < len(pb)-1:
        if pb[i] == "0" and pb[i+1] == "0":
            certo = False
            break
if certo:
    while len(pb) != 0:
        i = 0
        try:
            if pb[i] == "1" and pb[i+1] == "0" and pb[i+2] == "1":
                for x in range(2):
                    pb.pop(0)
                s += 1
            elif pb[i] == "1" and pb[i+1] == "1" and pb[i+2] == "0":
                pb.pop(0)
                s += 1
            elif pb[i] == "1" and pb[i+1] == "1" and pb[i+2] == "1":
                for x in range(2):
                    pb.pop(0)
                s += 1
        except:
            try:
                if pb[i] == "1" and pb[i+1] == "1":
                    for x in range(2):
                        pb.pop(0)
                    s += 1
            except:
                if pb[i] == "1":
                    pb.pop(0)
    print(s)
else:
    print(-1)
