import os
os.system("cls || clear")





while True: #O loop fica mais aberto, se repetinfo enquanto for verdadeiro
    numero = float(input("\nInsira um número entre 0 e 10: "))

    if numero<0 or numero>10:
        print("\nNÚMERO INVALIDO")
        print("Tente novamente")
    else:
        break #Para o loop
print(f"Número inserido: {numero}")
print("=== FIM ===")