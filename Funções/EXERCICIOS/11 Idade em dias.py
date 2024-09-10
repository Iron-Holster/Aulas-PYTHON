"""
Faça uma função que receba a idade de uma pessoa em anos, meses e dias e retorna essa idade em dias
"""

import os
os.system("cls || clear")

def calculo (anos, meses, dias):
    resultado = (anos*365) + (meses * 30.437) + dias
    return resultado 


idade_anos = int(input("Insira seus ANOS de vida: "))
idade_meses = int(input("Insira seus MESES de vida: "))
idade_dias = int(input("Insira seus DIAS de vida: "))

dias = calculo(idade_anos, idade_meses, idade_dias)

print(f"Você está vivo á aproximadamente {dias:.2f} dias")
