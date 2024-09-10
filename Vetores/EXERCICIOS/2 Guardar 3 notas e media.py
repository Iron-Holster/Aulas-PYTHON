"""
Crie um programa que leia 3 notas, armazenando em um vetor e calcule a média aritimedica
"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 3
lista_notas=[]

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite sua nota: "))
    lista_notas.append(nota)

soma= sum(lista_notas) #sum() soma todos os números dentro do vetor
media = soma/QUANTIDADE_NOTAS

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas): #enumerate apresenta os números dentro da lista numerados pela ordem
    print(f"{contador+1} nota: {nota}")

print(f"Média: {media}")