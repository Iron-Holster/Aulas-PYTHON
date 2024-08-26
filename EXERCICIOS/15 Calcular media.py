import os
os.system("cls || clear")


resultado = 0
soma = 0

for i in range (5):
    nota = int(input(f"Insira a {i+1}° nota: "))

    soma = nota + soma
    resultado = soma /5
    
print (f"Resultado: {resultado}")