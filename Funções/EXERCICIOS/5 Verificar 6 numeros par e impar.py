"""
Crie uma função que receba um numero e mostre uma mensagem informando se o numero é par ou impar
"""

import os
os.system("cls || clear")
impares=0
pares=0

def verificar (n1):
    if (n1%2)!= 0:
        impares+=1
        print(f"quantidade de impares: {n1}")
    else:
        pares+=1
        print(f"quantidade de pares: {n1}")
        

print("=== Descubra se o número é impar ou par ===")
numero1 = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
numero3 = int(input("Insira um número: "))
numero4 = int(input("Insira um número: "))
numero5 = int(input("Insira um número: "))
numero6 = int(input("Insira um número: "))
