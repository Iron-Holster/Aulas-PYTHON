"""
Crie um programa que leia 4 notas, armazenando em um vetor e calcule a média aritimedica

verifique a situação do aluno considerando:
Média maior ou igual 7: aprovado
Média maior ou igual 5: recuperação
Média menor que 5: reprovado
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

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas): #enumerate apresenta os números dentro da lista numerados pela ordem
    print(f"{contador+1} nota: {nota}")

print(f"Média: {media}")
print(f"Estado do aluno: {situacao}")