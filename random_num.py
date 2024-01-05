import random
import numpy as np

r1 = random.random() # Gera números aleatórios entre 0 e 1
r2 = random.randrange(0,100) # Gera um número aleatório no intervalo especificado

print("\nNúmeros aleatórios: \n")
print(f"1º:{r1}, 2º:{r2}\n")

x = np.random.randint(0,100,(3,3)) # Gera um array com números aleatórios

print(f'Array criado: \n{x}')
