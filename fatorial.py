def fatorial(n): # Utilizando recursividade
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        return "Desculpe, não há fatorial para número negativo"
    else:
        return n*fatorial(n-1)
    
num = int(input("Informe o número: "))

fat = fatorial(num)

print("Fatorial de "+str(num)+" igual a "+str(fat))