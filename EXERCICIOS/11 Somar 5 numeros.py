import os
os.system("cls || clear")

#A soma precisa ter um valor atribuido a ela antes
soma = 0

for i in range (1,6):
    numero = int(input("Insira o número: "))
    #Essa conta abaixo faz com que mesmo tendo diversos numeros inseridos em apenas uma variavel, torna a soma entre eles possivel
    soma = numero + soma
    #A soma que antes não tinha valor, terá um atribuido a ela após os números serem somados
print (f"Resultado: {soma}")