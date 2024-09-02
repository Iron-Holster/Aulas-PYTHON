"""
Escreva um algoritimo que leia 3 notas de um aluno, caso o numero seja menor que 0 e maior que 10, mostre a pergunta novamente

após receber as notas dentro dos parametros acima, calcule a media e verifique se o aluno está aprovado, reprovado ou em recuperação

se a media for a partir de 7, aprovado
se a media for entre 5 e 6.9, recuperação
caso seja menor que 5, reprovado"""

import os
os.system("cls || clear")

quantidade_notas = 3
media = 0
soma = 0
notas = 0


for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Insira a {i+1}° do aluno: "))
            
        soma += nota
        media = soma/quantidade_notas

        if nota<0 or nota>10:
            print("\nNOTA INVALIDA")
            print("Tente novamente")
        else:
            break #Para o loop
print(f"\nMédia: {media}")

if media>=7.0:
    print("ALUNO APROVADO")
elif media>=5.0 and media<=6.9: 
    print("ALUNO EM RECUPERAÇÃO")
else:
    print("ALUNO REPROVADO")
    
print("=== FIM ===")