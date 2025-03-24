#Escreva um programa que leia o valor em metros e exiba convertido em centímetros e milimetros.

#==========================================================

num = float(input('Digite um valor em metros: '))
mm = num * 1000
cm = num * 100
dm = num * 10
dam = num / 10
hm = num / 100
km = num / 1000

print('Aqui está o valor em milímetros: {:.2f}mm\n'
      'Aqui está o valor em centímetros: {:.2f}cm\n'
      'Aqui está o valor em decímetros: {:.2f}dm\n'
      'Aqui está o valor em decâmetros: {:.2f}dam\n'
      'Aqui está o valor em hectômetros: {:.2f}hm\n'
      'Aqui está o valor em quilômetros: {:.3f}km\n'
      .format(mm, cm, dm, dam, hm, km))
