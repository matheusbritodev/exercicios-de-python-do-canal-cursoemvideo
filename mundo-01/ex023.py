'''#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Unidade = 4
Dezena = 3
Centena = 2
Milhar = 1'''
#==========================================================

num = int(input('Digite um número de 0 a 9999: '))
uni = num / 1 % 10
dez = num / 10 % 10
cen = num / 100 % 10
mil = num / 1000 % 10

print('O número {} pode ser dividido das seguintes formas:\nUnidade = {:.0f}\nDezena = {:.0f}\nCentena = {:.0f}\nMilhar = {:.0f}'.format(num, uni, dez, cen, mil))