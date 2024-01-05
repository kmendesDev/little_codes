# Para um ano ser bissexto ele deve ser:
# múltiplos de 4
# não múltiplos de 100
# exceto os múltiplos de 400

ano = int(input("Digite o ano: "))
if (ano%400==0)and(ano%100==0):
    print(f'\n{ano} é um ano bissexto !')
elif (ano%4==0)and(ano%100!=0):
    print(f'\n{ano} é um ano bissexto !')
else:
    print(f'\n{ano} não é um ano bissexto !')