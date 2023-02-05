while True:
    comprimento = int(input("Comprimento da Caixa: "))
    if 1 <= comprimento <= 100:
        break
while True:
    largura = int(input("Largura da Caixa: "))
    if 1 <= largura <= 100:
        break
while True:
    altura = int(input("Altura da Caixa: "))
    if 1 <= altura <= 100:
        break
while True:
    alturajanela = int(input("Altura da Janela: "))
    if 1 <= alturajanela <= 100:
        break
while True:
    largurajanela = int(input("Largura da Janela: "))
    if 1 <= largurajanela <= 100:
        break
caixa = [comprimento, altura, largura]
caixa.sort()
janela = [alturajanela, largurajanela]
janela.sort()
if caixa[0] <= janela[0] and caixa[1] <= janela[1]:
    print("S")
else:
    print("N")
