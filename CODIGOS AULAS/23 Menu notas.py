"""
Escreva um algoritimo que pergunte ao usuario se deseja inserie mais uma nota. Mostre um menu conforme descrito

S - Inserir mais uma nota
p - Ver quantas notas foram inseridas
N - Calcular a média aritimética das notas informadas

O programa deve mostrar a média aritimetica
"""
import os
os.system("cls || clear")

import os
import time

soma = 0
contador = 1
media = 0

while True:
    resposta = input ("""\n
    S - Inserir uma nota
    P - Ver quantas notas foram inseridas
    N - Calcular a média aritimética das notas informadas
    
    """).upper()
    
    match(resposta):
        case "S":
            nota = float(input("Insira uma nota: "))
            soma += nota
            contador += 1
        case "P":
            if contador == 0:
                print("Nenhuma nota foi inserida")
                print("Nenhuma nota foi inserida")
                
        case "N":
            