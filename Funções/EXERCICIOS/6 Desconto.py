"""
Fazer um programa que solicita o preço de um produto e infraciona esse preço em 10% 
se ele for menor que 100 e 20% se ele for maior ou igual a 100
"""

import os
os.system("cls || clear")

def calculo (n1):
    
    if n1<100:
        return  n1 -(0.10 * n1) 
    elif n1>=100:
        return n1 - (0.20 * n1)

valor_produto=float(input("Insira o preço do produto: "))

valor_final = calculo(valor_produto)


if valor_produto < 100:
    print(f""" |
    === Você recebeu um desconto de 10% ===
    Valor bruto: {valor_produto}
    Valor com desconto: {valor_final}
    """)
elif valor_produto >= 100:
    print(f""" |
    === Você recebeu um desconto de 10% ===
    Valor bruto: {valor_produto}
    Valor com desconto: {valor_final}
    """)