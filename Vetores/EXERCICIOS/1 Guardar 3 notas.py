"""
Crie um programa que leia 3 notas, armazenando em um vetor e mostre as notas informadas
"""

import os
os.system("cls || clear")

lista_notas=[]

for i in range (3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)  #insere a variavel dentro do vetor, criando uma especie de fila.

for note in lista_notas:
    print(f"Nota: {nota}")