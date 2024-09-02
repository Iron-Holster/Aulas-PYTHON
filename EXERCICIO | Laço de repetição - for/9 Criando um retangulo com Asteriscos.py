"""
Desenvolva um programa  que utilize dois laços 'for' (um dentro do outro) para imprimir um retangulo de 4 linhas por 6 colunas de asteriscos(*)
"""

import os
os.system("cls || clear")

for i in range(4):
    #laço para cada coluna dentro da linha. Vai imprimir 4 linhas do print dentro do proximo laço
    for j in range(6):
        # (end='') imprime asterisco sem pular linha
        print('*', end='')
    print()

