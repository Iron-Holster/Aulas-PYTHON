"""
Desenvolva um programa que conte quantos numeros negativos foram inseridos pelo usuario usando um laço while.
o programa deve parar quando o usuario inserir 0 ou um numero positivo.
mostre a quantidade de numeros negativos
"""

import os
os.system("cls || clear")

contador = 0

while True:
    numero=int(input("Insira um numero negativo(-): "))
    contador+=1
    print(f"Quantidade de números inseridos: {contador}")
    
    if numero>=0:
        print("=== FIM ===")
        break