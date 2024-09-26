import os
os.system("cls || clear") 
from dataclasses import dataclass

# Salvar um arquivo chamado: carteira_de_clientes.txt
#Fazer leitura de dados do arquivo carteira_de_clientes.txt

@dataclass
class Aluno:
    nome: str
    saldo: int