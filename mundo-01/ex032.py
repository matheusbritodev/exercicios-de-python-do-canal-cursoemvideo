"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
#==========================================================

from calendar import isleap
year = int(input('Digite um ano qualquer: '))

if isleap(year) == True:
    print('This  is a leap year!')
else:
    print('This is not a leap year!')

