import os
os.system("cls || clear")

quantidade_notas = 3 # Uma constante, isso auxilia caso vá alterar o codigo futuramente
media = 0
soma = 0

for i in range (quantidade_notas):
    nota = float(input(f"Insira a {i+1}° nota: "))

    soma = nota + soma
    media = soma / quantidade_notas
    
print (f"Média: {media}")

if(media>=7.0):
    print("Aluno APROVADO")
elif (media>=4.0):
    print("Aluno em RECUPERAÇÃO") # | elif = else + if | senão-se, podendo fazer um teste ao mesmo tempo que cai em outra condição. "Se não, faça outro teste"
else:
    print("Aluno REPROVADO")