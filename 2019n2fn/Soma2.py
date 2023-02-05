while True:
    n = str(input()).split()
    quantidade = int(n[0])
    valor_que_quer = int(n[1])
    valor = str(input()).split()
    if len(valor) == quantidade:
        break
tot = s = 0
for i in range(quantidade):
    s += int(valor[i])
    if s > valor_que_quer:
        s = 0
        print(i, "Passou do Limite e zerando a soma")
    if int(valor[i]) == valor_que_quer:
        tot += 1
        print(i, "Valor Igual")
    if s == valor_que_quer:
        tot += 1
        print(i, "Soma igual")
print(tot)

#1 1 1 1 1 5 12 1 0 1 1 1 51 1 1
