"""
Escreva um programa que permita ler 2 notas de um aluno e:

- Informe por meio de uma função a media

- Informe por meio de uma função se a média for maior ou igual a 7, o aluno será aprovado, caso contrário estará reprovado
"""

import os
os.system("cls || clear")

def calculo_media (n1,n2):
    return  (n1+n2)/2

def avaliar_aluno (media):
    if media>= 7.0:
        print("\nAluno Aprovado")
        print(f"Média: {media}")
    else:
        print("\nAluno Reprovado")
        print(f"Média: {media}")

nota1 = float(input("Insira a 1° nota do aluno: "))
nota2 = float(input("Insira a 2° nota do aluno: "))

media = calculo_media(nota1,nota2)

avaliar_aluno(media)
