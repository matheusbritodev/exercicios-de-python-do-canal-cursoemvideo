#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m².
#==========================================================

weight = float(input('Qual a LARGURA da parede em metros?'))
height = float(input('Qual a ALTURA da parede em metros?'))
a = weight * height
aInk = a / 2
print('A área da parede é {:.2f}x{:.2f}, a área total é de {:.2f}m² e são necessários {:.2f}L de tinta para pintar a parede.'.format(weight, height, a, aInk))

