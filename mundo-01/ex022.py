"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar os espaços.
Quantas letras tem o primeiro nome."""
#==========================================================

name = str(input("Digite o seu nome completo:")).strip()

print('Seu nome em letras MAIÚSCULAS = {}'.format(name.upper()))
print('Seu nome em letras minúsculas = {}'.format(name.lower()))
print('Quantas letras tem o seu nome completo = {}'.format(len(name.replace(' ', ''))))
print('Quantas letras tem apenas o primeiro nome = {}'.format(len(name.split()[0])))
#
#==========================================================
