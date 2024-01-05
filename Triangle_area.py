import os

os.system("clear")
def area(b,h):
    os.system("clear")
    a = b*h/2
    print(f"\nO triângulo de base {b} e altura {h} possui área igual a {a}.\n")

# Recebendo os valores da base e altura do triângulo:
b = float(input("\nDigite o valor da base do triângulo:"))
h = float(input("Digite o valor da altura do triângulo: "))

area(b,h)