"""
Crie um programa que solivite ao usuario seu login e senha
O programa deve continuar pedindo o Login e senha até que ambos estejam corretos
O programa deve solicitar login e senha apenas 3 vezes. caso ultrapasse o número de tentativas, o programa deve ser finalizado"""

import os
os.system("cls || clear")

nome_login = "VICTOR"
senha_login = "1234"
limite=0

while True:
    print("\n=== Faça seu Login ===")
    nome = input("Digite seu nome: ").upper().strip()
    senha = input("Digite sua senha: ").strip()
    
    limite+=1

    if nome == nome_login and senha == senha_login:
        print("BEM VINDO")
        break
    elif limite > 2:
        print("\n# LIMITE DE TENTATIVAS ATINGIDO #")
        break
    else: 
        print("\n# NOME DE USUARIO OU SENHA INCORRETOS #")
        print("Tente novamente")

print("=== FIM ===")