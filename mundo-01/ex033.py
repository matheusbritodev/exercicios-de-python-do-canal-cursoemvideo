"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor número.
"""
#==========================================================
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))
menor = num1
maior = num1

if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

if num3<num2 and num3<num1:
    menor = num3

if num2<num1 and num2<num3:
    menor = num2

print('O menor número é {}\n' 'O maior número é {}'.format(menor, maior))
