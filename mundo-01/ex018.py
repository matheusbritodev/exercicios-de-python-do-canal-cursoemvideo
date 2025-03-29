#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#==========================================================

from math import sin, cos,tan,radians
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(sen, cos, tan))
