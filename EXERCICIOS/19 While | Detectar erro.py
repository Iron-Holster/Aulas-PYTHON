import os
os.system("cls || clear")



numero = float(input("Insira um número entre 0 e 10: "))

while numero<0 or numero>10:
    
    print("\nNÚMERO INVALIDO")
    print("Tente novamente")
    
    numero = float(input("\nInsira um número entre 0 e 10: "))

print(f"Número inserido: {numero}")
print("=== FIM ===")