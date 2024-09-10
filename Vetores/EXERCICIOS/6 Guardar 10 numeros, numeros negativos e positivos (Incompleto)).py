"""
Crie um algoritimo que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor
"""

import os
os.system("cls || clear")


QUANTIDADE_NUMEROS = 10
lista_numeros=[]
lista_numeros_positivos=[]


quantidade_negativos=0
 

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite sua numeros: "))
    lista_numeros.append(numero)
    
    if numero <0:
        quantidade_negativos+=1  
    else:
        lista_numeros_positivos.append(numero) 
    

print("\n=== Exibindo resultados ===")
for contador, numero in enumerate(lista_numeros): #enumerate apresenta os números dentro da lista numerados pela ordem
    print(f"{contador+1} numeros: {numero}")

print(f"Quantidade de números negativos: {quantidade_negativos}")


print("=== NUMEROS POSITIVOS ===")
for contador, numero in (lista_numeros_positivos): #enumerate apresenta os números dentro da lista numerados pela ordem
    print(f"{contador+1} numeros: {numero}")
