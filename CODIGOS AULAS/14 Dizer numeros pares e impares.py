import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Insira um número: "))
    # "%" significa que o resto da divisão de um numero. que no caso, se for igual a zero, o numero é par
    if numero % 2 == 0: 
        pares = pares + 1
    else:    
        impares = impares + 1

print(f"Quantidade de pares: {pares}")    
print(f"Quantidade de pares: {impares}")    