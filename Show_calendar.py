import calendar

y = int(input("Digite o ano: "))
m = int(input("Digite o mês(Número): "))

mes = calendar.month(y,m)
print("\n"+mes)