import os
os.system("cls || clear") 

#Comando utilizado para fazer loops, esse sendo um que usa o i e vai mudando pelo proximo número a cada loop
#Devesse colocar +1 no numero limite para indicar seu fim
#for i in range(1,11):
    #print(i)
print("=== TABUADA ===")
numero= int(input("Insira um número para ver sua tabuada: "))

#Letra i representa o numero que irá variar
for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")
#com isso dá pra fazer praticamente qualquer conta em massa
#a ação de "mudar de valor" = iterar