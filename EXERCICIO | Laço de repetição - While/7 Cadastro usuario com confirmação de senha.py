"""
Crie um programa que solicite ao usuario criar uma senha.
O programa deve pedir para confirmar a senha e garantir que ambas as senhas coicidam.
Se as senhas não coicidirem, o programa deve continuar pedindo ao usuario inserir e confirmar a senha até que ambas senham iguais.
"""

import os
os.system("cls || clear")

print("=== Altere sua Senha ===")

while True:
    nova_senha = input("\nInsira nova senha: ")
    check_senha = input("Confirme a senha: ")

    if nova_senha == check_senha:
        print("Senha alterada com sucesso!")
        break
    else:
        print("Senhas não coicidem, tente novamente.")