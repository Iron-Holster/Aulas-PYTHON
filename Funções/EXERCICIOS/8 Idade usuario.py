"""
Escreva um programa que solicite ao usuario o ano de nascimento e, 
utilizando uma função retorn com a idade do usuario.
"""

import os
os.system("cls || clear")

def calculo_idade (Data):
    ano_atual = 2024
    return (ano_atual-Data)

data=int(input("Insira sua data de nascimento: "))

idade = calculo_idade(data)

print(f"\nVocê tem {idade} Anos de idade.")