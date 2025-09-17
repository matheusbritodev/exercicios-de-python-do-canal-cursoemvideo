"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo = int(input("Digite o primeiro termo:\n> "))
razao = int(input("Digite a razão:\n> "))
loop = 10

while loop > 0:
    print(f"{termo} ", end="")
    termo += razao
    print(" --> " if loop > 1 else "", end="")
    loop-= 1
print("--> FIM")