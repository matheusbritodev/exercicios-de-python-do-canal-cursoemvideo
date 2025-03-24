#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
#==========================================================

num = int(input('Digite um número inteiro: '))
print('-' * 17,
      '\n{} x {:2} = '.format(num, 1),num * 1,
      '\n{} x {:2} = '.format(num, 2), num * 2,
      '\n{} x {:2} = '.format(num, 3), num * 3,
      '\n{} x {:2} = '.format(num, 4), num * 4,
      '\n{} x {:2} = '.format(num, 5), num * 5,
      '\n{} x {:2} = '.format(num, 6), num * 6,
      '\n{} x {:2} = '.format(num, 7), num * 7,
      '\n{} x {:2} = '.format(num, 8), num * 8,
      '\n{} x {:2} = '.format(num, 9), num * 9,
      '\n{} x {:2} = '.format(num, 10), num * 10)
print('-' * 17)