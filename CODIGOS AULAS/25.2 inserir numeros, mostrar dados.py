"""
Crie um algoritimo que leia 5 números inteiros e, em seguida mostre na tela:

1 - A quantidade de números Pares;
2 - A quantidade de números Ímpares;
3 - A quantidade de números Positivos;
4 - A quantidade de números Negativos

"""

import os
os.system("cls || clear")

QUANTIDADE_NUM = 5
num_pares = []
num_impares = []
num_positivos = []
num_negativos = []
num_geral = []
contador = 1

while True:
    numero = int(input(f"Insira o {contador}° número: "))
    contador += 1

    num_geral.append(numero)

    if numero > 0:
        num_positivos.append(numero)
    else: 
        num_negativos.append(numero)

    if numero%2 == 0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)

    if numero == 0:
        break

print("=== DADOS ANALIZADOS ===")
print(f"""
Quantidade de números: {len(num_geral)}
Quantidade de números Pares: {len(num_pares)}
Quantidade de números Ímpares: {len(num_impares)}
Quantidade de números Positivos: {len(num_positivos)}
Quantidade de números Negativos: {len(num_negativos)}
""")