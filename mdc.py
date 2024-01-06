print("\nCálculo de MDC:\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

menor = a 
if a>b:
    menor = b

while(True):
    if (a%menor == 0)and(b%menor == 0):
        mdc = menor
        break
    menor -= 1

print (f'O MDC entre {a} e {b} é {mdc}')