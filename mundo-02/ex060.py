"""
Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

num_fatorial = int(input("Digite um número:\n> "))
resultado = 1
c = num_fatorial
print(f"Calculando {num_fatorial}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    resultado *= c
    c -= 1
print(resultado, end="")
