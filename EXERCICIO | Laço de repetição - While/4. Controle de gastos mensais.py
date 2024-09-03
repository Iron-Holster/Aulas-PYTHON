"""
Crie um programa que ajude o usuario a controlar seus gastos mensais.
o programa deve permitir que o usuario insira gastos diarios até que o gasto total do mes exceda o orçamento inicial fornecido.
o programa deve exibir o total gasto e o valor excedente
"""

import os
os.system("cls || clear")
gasto=0
limite= float(input(f"Insira seu limite: "))

while True:
    gasto += float(input("Insira seu gasto diario: "))

    resto = limite - gasto

   
    print(f"Ainda restam: {resto}")

    if gasto> limite:
        print("Limite excedido!")
        break
