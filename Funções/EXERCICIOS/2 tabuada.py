"""
Faça um programa que imprime a tabuada de um numero informado pelo usuario de 1 a 10
utilizando uma função para exibir o resultado
"""

import os
os.system("cls || clear")


def tabuada(n1):
    for i in range (1,11):
        print(f"{n1} x {i} = {n1 * i}")
        

print("=== TABUADA ===")
numero = int(input("Insira um número para ver sua tabuada: "))

tabuada(numero)

