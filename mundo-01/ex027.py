"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguido o primeiro e o último nome separadamente.
ex: Ana Maria de Souza
primeiro = Ana
Último = Souza
"""
#==========================================================
complete_name = str(input('Type your complete name: ')).strip().title().split()
print("Name: {}\nFirst name: {}\nLast name: {}".format(" ".join(complete_name), complete_name[0], complete_name[-1]))