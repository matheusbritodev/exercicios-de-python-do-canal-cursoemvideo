"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
"""

num = int(input("Digite um número:\n> "))

cont = 0
for n in range(1, num +1):
    if num % n == 0:
        cont += 1

if cont == 2:
    print(f"{num} é primo!")
else:
    print(f"{num} NÃO é primo!")