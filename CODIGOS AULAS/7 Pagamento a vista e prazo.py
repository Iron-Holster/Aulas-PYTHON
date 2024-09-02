import os
os.system("cls || clear") 


#Tela de compra e forma de pagamento
print("""=== GNOMOS DE JARDIM ===
pagamento a vista recebe 10% de desconto""")

pagamento = int(input("""
Selecione a forma de pagamento:
1 - Pagamento à vista
2 - Pagamento à Prazo

>"""))

match(pagamento):
    case 1:
        #Dados a vista não nescessitam calculo (Acredito eu né)
        print("""
    Pagamento a vista -
    Valor do produto: R$ 100.00
    Desconto: 10%
    Valor a pagar: R$ 90.00
    """)
    case 2:
        parcelas = int(input("""
    Valor por parcela: 16.66
    Maximo de parcelas: 6
    Quantidade a ser parcelada: """))
        #If impede que ultrapasse o limite
        if(parcelas>6):
            print("Quantidade de parcelas desejada ultrapassa o limite, Tente novamente.")
        else:
            valor_final = 100/parcelas
            #Calculo simples e exibição de resultado
            print(f"""
        Valor a pagar: {valor_final}
        Total a prazo: R$ 100.00""")
    case _:
        print("Opção invalida")