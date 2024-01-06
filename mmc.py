print("Calculo de MMC:\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

maior = a 
if a<b:
    maior = b

while(True):
    if (maior%a == 0)and(maior%b == 0):
        mmc = maior
        break
    maior += 1

print (f'O MMC entre {a} e {b} é {mmc}')