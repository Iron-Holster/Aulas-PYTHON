"""
Crie uma função que receba um numero e mostre uma mensagem informando se o numero é par ou impar
"""

import os
os.system("cls || clear")

def verificar (n1):
    if (n1%2)!= 0:
        print("Impar!")
    else:
        print("Par!")


numero = int(input("Insira um numero para saber se é par ou impar: "))

verificar(numero)
