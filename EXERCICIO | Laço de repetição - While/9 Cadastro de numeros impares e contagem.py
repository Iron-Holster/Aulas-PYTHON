"""
Crie um programa que peça ao usuario para inserir numeros inteiros até que a soma dos numeros impares inseridos seja maior que 200. 
o programa deve exibir o total de numeros impares inseridos e a soma desses numeros
"""

import os
os.system("cls || clear")
soma=0
impares=0
pares=0
numeros=0
contador=0

print("Insira numeros impares que somem até atingir a meta de 200")
while True:
    numeros=int(input("\nInsira um numero: "))

    if (numeros%2) != 0: # %2 significa: "Se o numero foi divisivel por 2"
        impares+=numeros
    else:
        print("Insira apenas números impares")
        pares+=1
    
    soma += impares

    if soma > 200:
       print(f"""
        Meta atingida! {soma}
        Números Invalidos (pares) inseridos: {pares}""")
       break
   
       
