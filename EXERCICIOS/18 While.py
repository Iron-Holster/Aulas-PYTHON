import os
os.system("cls || clear")

continua = "S"
contador = 0
# Enquanto a condição desejada for verdadeira, o programa irá repeti-la
while continua == "S":
    print("Repetindo...")
    contador += 1


    continua = input("tecle 'S' para continuar: ").upper()

if contador == 0:
    print("O bloco NÃO foi repetido")
else:
    print(f"O bloco foi repetido {contador} vezes")