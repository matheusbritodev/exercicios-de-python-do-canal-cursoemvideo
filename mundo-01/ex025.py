#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Martins" no nome.
#==========================================================
name = str(input('What is your complete name? ')).strip()
print('Seu nome tem Martins? {}'.format('martins' in name.lower()))