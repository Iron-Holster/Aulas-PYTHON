"""
Crie funções que recebam 2 numeros e retorne com a soma, subtração, multiplicação e divisão dos números
"""

import os
os.system("cls || clear")

def soma (n1,n2):
    print("== Soma ==")
    print(f"{n1} + {n2} = {n1+n2}")
    return soma

def subtraçao (n1,n2):
    print("== Subtração ==")
    print(f"{n1} - {n2} = {n1-n2}")
    return soma

def divisao (n1,n2):
    print("== Divisão ==")
    print(f"{n1} / {n2} = {n1/n2}")
    return soma

def multiplicacao (n1,n2):
    print("== Multiplicação ==")
    print(f"{n1} x {n2} = {n1*n2}")
    return soma

print("Insira 2 números e veja os possiveis calculos entre ambos")
numero1 = int(input("Insira o número: "))
numero2 = int(input("Insira o número: "))
                
soma = soma(numero1,numero2)
subtraçao = subtraçao(numero1,numero2)
divisao = divisao(numero1,numero2)
multiplicacao = multiplicacao(numero1,numero2)

(soma)
(subtraçao)
(divisao)
(multiplicacao)
