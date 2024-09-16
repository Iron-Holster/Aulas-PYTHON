"""

"""

import os
os.system("cls||clear")

QUANTIDADE_NUMEROS = 6
lista_pares_positivos = []

print("\n === Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input(f"Digite o {i+1} número: "))

        if numero%2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("Número inválido. \nTente Novamente \n\n")

print("\n === Exibindo dados ===")
for i, numero in enumerate(reversed(lista_pares_positivos)):
    print(f"{len(lista_pares_positivos)-i}° - {numero}")