"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

num1 = int(input("Digite um número:\n> "))
num2 = int(input("Digite outro número:\n> "))

maior_valor = 0
menor_valor = 0
if num2 == num1: 
    print("Os dois números são iguais.")
else:
    if num1 > maior_valor < num2: 
        maior_valor = num1
        menor_valor = num2
    if num2 > maior_valor: 
        maior_valor = num2
        menor_valor = num2 
    print(f"O maior valor é: {maior_valor}\nO menor valor é: {menor_valor}")
