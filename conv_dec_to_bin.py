#Conversão de um numéro decimal para binário:

num = 10051
binario = ""
cociente = num
print(binario)
#Primeira maneira:
while cociente != 0:
    
    if cociente%2 == 0:
        resto = "0"
    else:
        resto = "1"
    binario = resto + binario
    cociente=int(cociente/2)
    #print(binario)

print(binario)

# Segunda maneira:
print("\n"+bin(num))