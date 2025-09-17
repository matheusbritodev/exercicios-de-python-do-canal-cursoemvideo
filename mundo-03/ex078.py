"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = []
maior = 0
menor = 0
cont = 1

for i in range(5):
    numeros.append(int(input("Digite um número: ")))
for n in numeros:
    if cont > 0:
        maior = n
        menor = n
        cont -= 1
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f"\nMAIOR: {maior}, POSIÇÃO: {numeros.index(maior) + 1}\nMENOR: {menor}, POSIÇÃO: {numeros.index(menor) + 1}")