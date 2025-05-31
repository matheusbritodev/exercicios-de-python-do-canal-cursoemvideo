"""
Crie um programa que leia um número inteiro e mostre na tela se ele é "PAR" ou "ÍMPAR".
"""
#==========================================================
numTyped = int(input("Digite um número inteiro aleatório: "))
if numTyped % 2 == 0 :
    print("Esse é um número PAR")
else:
    print("Esse é um número ÍMPAR")