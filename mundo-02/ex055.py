"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
peso_maior = 0
peso_menor = 0

for indice in range(1, 6):
    peso_pessoa = float(input(f"Peso da {indice}ª pessoa:\n> "))
    if indice == 1:
            peso_maior = peso_pessoa
            peso_menor = peso_pessoa
    else:
        if peso_pessoa > peso_maior:
            peso_maior = peso_pessoa
        elif peso_pessoa < peso_menor:
            peso_menor = peso_pessoa
print(f"PESO MAIOR: {peso_maior}kg")
print(f"PESO MENOR: {peso_menor}kg")

