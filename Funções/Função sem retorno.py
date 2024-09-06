import os
os.system("cls || clear")

# === Funções sem retorno ===

def logo_senai(): #Cria uma variavel que guarda um codigo
    os.system("cls || clear")
    print("""
    =============
    --  SENAI  --
    =============
    """)

logo_senai() #executa o codigo armazenado
nome= input("Digite seu nome: ")
logo_senai()
idade= input("Digite sua idade: ")
logo_senai()
nota= input("Digite sua nota: ")