def swap1(a,b):
    temp = a
    a = b
    b = temp
    print("\nVariáveis trocadas no swap1: \n")
    print(f'a={a}')
    print(f'b={b}')

def swap2():
    global a
    global b
    a,b = b,a # Sem usar variável temporária
    print("\nVariáveis trocadas no swap2: \n")
    print(f'a={a}')
    print(f'b={b}')


a = input("Digite a primeira variável: ")
b = input("Digite a segunda variável: ")
print("\nVariáveis iniciais: \n")
print(f'a={a}')
print(f'b={b}\n')

swap1(a,b)
print(a,b)

swap2()
print(a,b)

