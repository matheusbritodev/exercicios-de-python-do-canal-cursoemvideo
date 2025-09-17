"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

lado1 = float(input("Digite o tamanho do lado 1:\n> "))
lado2 = float(input("Digite o tamanho do lado 2:\n> "))
lado3 = float(input("Digite o tamanho do lado 3:\n> "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os segmentos acima PODEM FORMAR um triângulo")
    if lado1 == lado2 and lado1 == lado3: print("EQUILÁTERO")
    elif lado1 != lado2 != lado3: print("ESCALENO")
    else: print("ISÓSCELES")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")