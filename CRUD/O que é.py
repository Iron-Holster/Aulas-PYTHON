import os
os.system("cls || clear") 

#CRUD

#C reate  
#R ead    
#U pdate  
#D elete 

#Estrutura de dados

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 0

lista_alunos = []
#Solicitando dados
for i in range (QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Insira seu nome: "),
        idade = int(input("Insira sua idade: "))
    )
    lista_alunos.append(aluno)
#Exibindo dados
for aluno in lista_alunos:
    print(f" Nome: {aluno.nome}")
    print(f" Idade: {aluno.idade}")
    

nome_arquivo = "Lista_de_alunos.txt"

with open(nome_arquivo, "w") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.idade}")