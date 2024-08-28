"""
Escreva um algoritimo que solicite 2 notas para o aluno
Caso seja menor que o 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a media aritimetica do aluno.
"""

import os
os.system("cls || clear")

quantidade_notas = 2
media = 0
soma = 0
notas = 0

#Caso deseje utilizar "for i in range" toda a parte "While" deve estar dentro de seu laço de repetição

while True:
    nota1 = float(input(f"\nInsira a primeira nota do aluno: "))
    nota2 = float(input(f"Insira a segunda nota do aluno: "))
        
    soma = nota1 + nota2
    media = soma/quantidade_notas

    #if (nota1<0 or nota1>10) or (nota2<0 or nota2>10):
    #    print("\nALGUMA NOTA É INVALIDA")
    #    print("Tente novamente")

    if nota1<0 or nota1>10:
        print("\nALGUMA NOTA É INVALIDA")
        print("Tente novamente")
    elif nota2<0 or nota2>10:
        print("\nALGUMA NOTA É INVALIDA")
        print("Tente novamente")
    else:
        break #Para o loop
print(f"Média: {media}")
print("=== FIM ===")