"""
Crie um programa que leia 6 números, armazenando em um vetor e informe quantos são pares e quantos são ímpares
mostres os números informados pelo usuario
"""

import os
os.system("cls || clear")


QUANTIDADE_NOTAS = 6
lista_notas=[]

par_contador=0
impar_contador=0
 

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    nota = int(input("Digite sua nota: "))
    lista_notas.append(nota)
    
    if nota % 2 != 0:
        impar_contador+=1  
    else:
        par_contador+=1  
    

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas): #enumerate apresenta os números dentro da lista numerados pela ordem
    print(f"{contador+1} nota: {nota}")

print(f"Quantidade de números impares: {impar_contador}")
print(f"Quantidade de números pares: {par_contador}")