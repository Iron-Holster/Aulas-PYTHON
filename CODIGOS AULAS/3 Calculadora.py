import os
os.system("cls || clear") 

#Menu
print("=== CALCULADORA ===")
print("""
      1 - Soma (+)
      2 - Subtração (-)
      3 - Multiplicação (*)
      4 - Divisão (/)
      """)
tipo = int(input("Selecione o tipo de cálculo desejado:"))
 
 #Opções, calculos e respostas derivadas
match (tipo):
    case 1:
        print("=== SOMA ===")

        soma1 = int(input("Digite o Primeiro número:"))
        soma2 = int(input("Digite o Segundo número:"))
        soma_result = soma1 + soma2

        print (f"{soma1} + {soma2} = {soma_result}")
    case 2:
        print("=== SUBTRAÇÃO ===")
        sub1 = int(input("Digite o Primeiro número:"))
        sub2 = int(input("Digite o Segundo número:"))
        sub_result = sub1 - sub2

        print (f"{sub1} - {sub2} = {sub_result}")
        
    case 3:
        print("=== MUTIPLICAÇÃO ===")
        mult1 = int(input("Digite o Primeiro número:"))
        mult2 = int(input("Digite o Segundo número:"))
        mult_result = mult1 * mult2

        print (f"{mult1} x {mult2} = {mult_result}")

    case 4:
        print("=== DIVISÃO ===")
        divi1 = int(input("Digite o Dividendo:"))
        divi2 = int(input("Digite o Divisor:"))
        divi_result = divi1 / divi2

        print (f"{divi1} ÷ {divi2} = {divi_result}")
    
    case _:
        print("Opção invalida")
