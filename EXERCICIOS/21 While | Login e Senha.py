"""
Crie um programa que solivite ao usuario seu login e senha
O programa deve continuar pedindo o Login e senha até que ambos estejam corretos"""

import os
os.system("cls || clear")

nome_login = "VICTOR"
senha_login = "1234"

while True:
    print("\n=== Faça seu Login ===")
    nome = input("Digite seu nome: ").upper().strip()
    senha = input("Digite sua senha: ").strip()

    if nome == nome_login and senha == senha_login:
        print("BEM VINDO")
        break
    else: 
        print("\n# NOME DE USUARIO OU SENHA INCORRETOS #")
        print("Tente novamente")
print("=== FIM ===")