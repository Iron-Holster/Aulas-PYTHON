import os
os.system("cls || clear") 
    
print("=== CALCULE O PESO IDEAL ===")
print("F para feminino e M para Masculino")
genero=input("Insira seu gênero: ")

match(genero):
    case "M" | "m":
        altura=float(input("Insira sua altura: "))
        peso_ideal= (72.7*altura)-58
        print(f"Peso ideal: {peso_ideal}")
    
    case "F" | "f":
        altura=float(input("Insira sua altura: "))
        peso_ideal= (62.1*altura)- 44.7
        print(f"Peso ideal: {peso_ideal}")