#Crie um progama onde solicite a idade do usuario e exiba o resultado. levando em conta que menores de 18 anos não obrigados a votar
# e pessoas maiores de 65 não são obrigadas
import os
os.system("cls || clear") 

print("=== DESCUBRA SE VOCÊ É OBRIGADO A VOTAR ===")
idade = int(input("Insira sua idade: "))

if idade >= 18 and idade <= 65:
    print("É OBRIGADO A VOTAR")
else:
    print("NÃO É OBRIGADO A VOTAR")
    
