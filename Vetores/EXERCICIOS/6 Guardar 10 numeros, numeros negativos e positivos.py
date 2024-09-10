"""
Crie um algoritimo que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor
"""

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 10
lista_notas=[]

negativos=[]
positivos=[]
 

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    nota = int(input("Digite sua nota: "))
    lista_notas.append(nota)
    
    if nota < 0:
        negativos.append(nota)  
    else:
        positivos.append(nota)  
    
quantidade_positivos = len(positivos)
quantidade_negativos = len(negativos)

print("\n=== Exibindo resultados ===")
for contador, nota in enumerate(lista_notas): 
    print(f"{contador+1} nota: {nota}")

print(f"Quantidade de números positivos: {quantidade_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")