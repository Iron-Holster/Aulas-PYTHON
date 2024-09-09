"""
Escreva um programa que solicite ao utilizador o fornecimento do seu peso em Kg e de sua altura em m 
e a partir deles calcule o indice de massa corporea do utilizador
"""

import os
os.system("cls || clear")

def calculo_imc(altura, peso):
    return peso/(altura*altura)

print("=== Saiba seu Índice de massa corpórea ===")
print(" Utilize ponto (.)")
altura = float(input("Digite sua altura(m): "))
peso = float(input("Digite seu peso(Kg): "))

imc = calculo_imc(altura, peso)

print(f"Seu índice de massa corporal é {imc:.2f}") # (:.2f) evita frações gigantes

#Abaixo do peso
if imc < 18.5:
    print("Você está abaixo do peso! \nConsulte um nutricionista")

#peso normal
elif imc >= 18.5 and imc < 25:
    print("Seu peso está normal! \nMatenha seus habitos saudáveis")

#Sobrepeso
elif imc >= 25 and imc < 30:
    print("Seu peso está com sobrepeso! \nConsidere uma dieta balaceada e atividade física")

#Obesidade 1
elif imc >= 30 and imc < 35:
    print("Seu peso está com Obesidade grau 1! \nProcure orientação de um profissional de saúde")
#Obesidade 2
elif imc >= 35 and imc < 40:
     print("Seu peso está com Obesidade grau 2! \nConsulte um médico para avaliação e orientação")

#Obesidade 3
elif imc >= 40:
     print("Seu peso está com Obesidade grau 3! \nBusque assistência médica imediatamente")


