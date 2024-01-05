def Convert(d):
    d = d*0.621371 # 1 milha é 0.621371 km
    print(f'\nA distância em milhas é {d} NM')

d = float(input("\nInforme a distância em quilômetros: "))
Convert(d)
