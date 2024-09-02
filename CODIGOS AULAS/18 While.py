import os
os.system("cls || clear")

continua = "S"
contador = 0
# Enquanto a condição desejada for verdadeira, o programa irá repeti-la

continua = input("tecle 'S' para continuar: ").upper()

while continua == "S":
    print("Repetindo...")
    
    contador += 1
    #Contador vai receber +1 (Contador = Contador + 1)

    continua = input("tecle 'S' para continuar: ").upper() #Caso esse input esteja fora da dentição, o Wjile irá gerar um loop infinito (CTRL+C pra parar)

if contador == 0:
    print("O bloco NÃO foi repetido")
else:
    print(f"O bloco foi repetido {contador} vezes")