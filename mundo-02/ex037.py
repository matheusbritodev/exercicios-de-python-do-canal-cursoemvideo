"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

num = int(input("Digite um número:\n> ")) #Escolha do número
choice = int(input(f"Escolha uma base de conversão para o número {num}:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n> ")) #

match choice:
    case 1:
        
        print(f"Resultado em binário: {bin(num)[2:]}")
    case 2:
        print(f"Resultado em octal: {oct(num)}")
    case 3:
        print(f"Resultado em hexadecimal: {hex(num)}") 
    case _:
        print("Opção inválida")