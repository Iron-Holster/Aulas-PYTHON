import os
os.system("cls || clear")

def calcular_media(n1,n2):
    media = (n1 + n2)/2
    return media

nota1 = float(input("Insira sua nota: "))
nota2 = float(input("Insira sua nota: "))

media = calcular_media(nota1, nota2)

print(f"Média: {media}")