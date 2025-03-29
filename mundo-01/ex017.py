#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#==========================================================

from math import sqrt
catAdj = float(input('Digite o valor do cateto adjacente: '))
catOpo = float(input('Digite o valor do cateto oposto: '))
hipo = (catAdj ** 2) + (catOpo ** 2)
hipoRaiz = math.sqrt(hipo)

print("O comprimento do cateto ADJACENTE é {:.2f} e o comprimento do cateto OPOSTO é {:.2f}, devido a isso o valor da hipotenusa é: {:.2f}".format(catAdj, catOpo, hipoRaiz))

#Alternativa mais eficiente
'''
from math import hypot
co = float(input('Digite o valor do cateto adjacente: '))
ca = float(input('Digite o valor do cateto oposto: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''