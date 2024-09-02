"""
Escreva um programa que use o laço 'While' para encontrar o primeiro numero maior que 50 que seja divisivel por 7. exiba esse número
"""

import os
os.system("cls || clear")

while True:
    numero=float(input("\nInsira um número maior que 50 e seja divisivel por 7: "))

    if numero <50 and (numero/7!=0):
        print("Número invalido, tente novamente")
    else:
        resultado = numero/7
        print(f"Número correto: {numero}")
        print(f"Resultado: {resultado}")
        break