def imc_calc(peso,alt):
    imc = peso/alt**2
    if imc<=18.5:
        nivel = "abaixo do peso"
    elif imc <= 24.9:
        nivel = "normal"
    elif imc <= 29.29:
        nivel = "sobrepeso"
    else:
        nivel = "obesidade"
    return imc,nivel

print("\nCalculador de IMC: ")
peso = float(input("Digite o peso: "))
alt = float(input("Digite a altura: "))

i,n = imc_calc(peso,alt)

print(f"O IMC resultou em: {i}, indicando: {n}")