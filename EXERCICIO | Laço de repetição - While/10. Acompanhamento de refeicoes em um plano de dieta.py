"""

"""

import os
os.system("cls || clear")
horas = 0

meta = 2000

while True:
    calorias += float(input("Insira horas estudadas hoje: "))

    resto = meta - calorias

    if calorias >= meta:
        print("Meta atingida!")
        print(f"Horas extras: {resto}")
        break
   
    print(f"Ainda restam: {resto} Horas")
