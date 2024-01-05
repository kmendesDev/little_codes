num=int(input("Digite o número: "))

sinal = False

if num>1: # 1 não é primo
    for i in range(2,num):
        if num%i==0:
            sinal = True
else: 
    sinal = True
if sinal:
    print(f'{num} não é um número primo')
else: 
    print(f'{num} é um número primo')