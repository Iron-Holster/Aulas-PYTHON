"""
Crie uma função que receba um numero e mostre uma mensagem informando se o numero é par ou impar
"""

import os
os.system("cls || clear")


def verificar ():
    impares=0
    pares=0

    for i in range(1,7):
        numero =int(input("Digite um numero: "))

        if numero%2 == 0:
            pares+=1    
        else:
            impares+=1

    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de impares: {impares}")

verificar()