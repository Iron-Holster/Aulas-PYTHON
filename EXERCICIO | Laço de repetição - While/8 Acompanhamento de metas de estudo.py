"""
Crie um programa para ajudar o usuario a acompanhar suas metas de estudo.
O usuario define uma meta de horas e o programa deve permitir que o usuario insira o numero de horas estudadas até que atinja o total ou exceda a nota
o programa deve exibir o total de horas estudadas e o valor excedente
"""

import os
os.system("cls || clear")
horas = 0

meta = float(input(f"Insira sua meta de horas de estudo: "))

while True:
    horas += float(input("Insira horas estudadas hoje: "))

    resto = meta - horas

    if horas >= meta:
        print("Meta atingida!")
        print(f"Horas extras: {resto}")
        break
   
    print(f"Ainda restam: {resto} Horas")
