"""
Escreva um algoritimo que pergunte ao ususario se deseja inserir mais uma nota, se a resposta for "N" o programa fará a media com as notas informadas

OBS: use um contador dentro do laço para contar a quantidade de iterações
"""

import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("Insira uma nota: "))
    
    contador += 1
    soma += nota

    resposta = input ("""Deseja inserir mais uma nota? S ou N  
                      """).upper()
    if resposta == "N":
        break

media = soma/contador
print(f"Media: {media}")
