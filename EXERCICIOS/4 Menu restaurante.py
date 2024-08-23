import os
os.system("cls || clear") 

print("=== BEM VINDO ===")
print("""
      1 - Picanha
      2 - Lasanha
      3 - Strogonoff
      4 - Bife Acebolado
      5 - Pão com ovo
      """)

opcao = int(input ("Selecione seu prato: "))

match(opcao):
    case 1:
        print("""
    Prato selecionado: Picanha
    Valor: R$ 25.00
              """)
    case 2:
        print("""
    Prato selecionado: Lasanha
    Valor: R$ 20.00
              """)

    case 3:
        print("""
    Prato selecionado: Strogonoff
    Valor: R$ 18.00
              """)
        
    case 4:
        print("""
    Prato selecionado: Bife acebolado
    Valor: R$ 15.00
              """)
 
    case 5:
        print("""
    Prato selecionado: Pão com ovo
    Valor: R$ 5.00
              """)
    case _:
        print("Código de prato inexistente ou invalido")

resposta = input("""
Finalizar compra? S ou N
4
                """)

if resposta == "s":
    print("- OK! Seu pedido está a caminho -")
if resposta == "n":
    print("- Volte sempre! -")