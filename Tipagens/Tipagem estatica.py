import os

os.system("cls || clear") #Limpa o console

# Tipagem estática
nome : str # cadeia
idade : int # inteiro
altura : float # real

nome = "Mario"
idade = 42
altura = 1.72

#print = escreva
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"altura: {altura}")
# o f no inicio e as chaves {} na variavel incluem a variavel no texto sem ter problemas com sua tipagem

#Vantagem: Maior organização entre os tipos de variaveis, recomendado em projetos grandes