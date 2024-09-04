"""
Crie um programa que ajude um estudante a calcular a media de suas notas.
O programa deve permitir que o usuario insira notas de provas até que insira um numero negativo.
O programa deve calcular e exibir a media das notas inseridas.
"""

import os
os.system("cls || clear")

soma = 0
contador = 0
while True:
    notas = float(input("Insira a nota do aluno (Insira uma nota negativa para receber a média): "))
    
    if notas < 0:
        break
    
    soma += notas
    contador += 1
    
    


media = soma / contador
print(f"Média: {media}")
