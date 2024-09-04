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

# === Funções com retorno ===

os.system("cls || clear")
def somar (n1,n2): #Variaveis dentro dos parenteses podem ser alterados
    soma = n1 + n2 # a variavel soma que está aq, não esta relacionada com a variavel lá no final. já que estão em planos diferentes
    return soma #Retorna o resultado para onde a função foi convocada

primeiro_numero=int(input("Digite um numero: "))
segundo_numero=int(input("Digite um numero: "))
soma = somar(primeiro_numero, segundo_numero) #Pode-se colocar variaveis para serem utilizadas na função
print(f"Soma: {soma}")

# == Exemplo - Função com retorno ===

os.system("cls || clear")
def descontos_salario(salario_bruto):
    vale_transporte = 200
    vale_refeição = 150
    plano_de_saude = 300

    resultado = salario_bruto - (vale_transporte + vale_transporte + vale_refeição + plano_de_saude)
    return resultado

salario_bruto = float(input("Digite o valor do seu salario bruto: "))

salario_liquido = descontos_salario(salario_bruto)

print(f"Salario liquido: {salario_liquido}")