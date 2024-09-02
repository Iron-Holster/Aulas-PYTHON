import os
os.system("cls || clear") 

print("Digite o número do dia da semana:")
dia = int(input())

match (dia):
    case 1:
        print("""Domingo
- Final de semana""")
        
    case 2:
        print("""Segunda-feira
- Dia util""")
        
    case 3:
        print("""Terça-feira
- Dia util""")
    
    case 4:
        print("""Quarta-feira
- Dia util""")
    
    case 5:
        print("""Quinta-feira
- Dia util""")
       
    case 6:
        print("""Sexta-feira
- Dia util""")

    case 7:
        print("""Sábado
- Final de semana""")
    
    case _:
        print("Dia invalido")