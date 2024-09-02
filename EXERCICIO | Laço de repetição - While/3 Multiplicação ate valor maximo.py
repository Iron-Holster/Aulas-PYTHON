"""
Escreva um programa que use o laço 'While' que multiplique um numero inicial por um fator dado pelo usuario até que exceda 100.
exiba o produto final e o numero de multiplicações realizadas
"""

import os
os.system("cls || clear")

num_inicial = 5
contador=0
while True:
    num_usu=float(input("\nInsira um numero que exceda 100 ao ser multiplicado por 5: "))
    
    contador+=1
    resultado= num_usu*num_inicial

    if resultado < 100:
        print("Número inferior a 100, Tente novamente") 
    else:
        print(f"""
    Calculo:
    {num_usu} x {num_inicial} = {resultado}
    
    Quantidade de calculos feitos: {contador}
    """)
        break