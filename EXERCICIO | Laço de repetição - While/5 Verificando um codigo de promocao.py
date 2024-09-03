"""
Desenvolva um programa que solicite ao usuario inserir um codigo de promoção para obter um desconto.
O codigo correto é "PROMO2024".
o usuario tem 3 tentativas para acertar.
Se o codigo estiver correto, exiba uma mensagem de "Codigo aceito" e o desconto.
se o usuario errar o codigo nas 3 tentativas, exiba uma mensagem de "Codigo invalido"
"""

import os
os.system("cls || clear")

cupom = "PROMO2024"
contador=0

while True:
    
    codigo_usu = input("Insira o cupom para receber o desconto: ")
    contador+=1
    if codigo_usu!=cupom:
        print("\nNÚMERO INVALIDO")
        print("Tente novamente")
        if contador>2:
            print("Limite de tentativas excedido!")
            break
    else:
        print("Parabens! Você recebeu 25% de desconto")
        break

    
    