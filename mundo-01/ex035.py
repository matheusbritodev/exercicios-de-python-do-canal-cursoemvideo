"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
lado1 = float(input("Digite o tamanho do lado 1:\n> "))
lado2 = float(input("Digite o tamanho do lado 2:\n> "))
lado3 = float(input("Digite o tamanho do lado 3:\n> "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os segmentos acima PODEM FORMAR um triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")

