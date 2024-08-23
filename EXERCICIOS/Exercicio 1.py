#CRIE UM CODIGO ONDE SOLICITE AO USUARIO NOME E SENHA, RECEBENDO UMA MENSAGEM SE BEM VINDO CASO ESCRITO CORRETAMENTE E UMA MENSAGEM DE ERRO 
import os
os.system("cls || clear") 

print("=== Faça seu Login ===")
nome_login = input("Digite seu nome: ")
senha_login = input("Digite sua senha: ")

if nome_login == "Victor" and senha_login == "1234":
    print("BEM VINDO")
else: 
    print("SENHA OU NOME DE USUARIO INCORRETOS")
