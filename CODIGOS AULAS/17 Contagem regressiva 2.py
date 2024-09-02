import os
os.system("cls || clear")

import os
import time #importa o programa que conta o tempo

os.system("cls || clear")

numero=int(input("Insira um numero para iniciar a contagem regressiva:"))
for i in range(numero,0,-1): #colocando -1, a maquina vai subtrair o proximo numero
    print(i)
    time.sleep(1) 