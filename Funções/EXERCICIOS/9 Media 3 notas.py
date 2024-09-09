"""
Escreva um programa que permita ler 3 notas de um aluno, usando laço de repetição e informe por meio de uma função a media
"""

import os
os.system("cls || clear")

notas=0

def calculo_media (n1):
    return  (n1)/3

for i in range(1,4):
    notas += float(input(f"Insira a {i}° nota do aluno: "))
    
media = calculo_media(notas)

print(f"Média: {media}")


