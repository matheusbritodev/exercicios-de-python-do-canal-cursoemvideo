#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#==========================================================

from random import shuffle
name1 = str(input('Digite o nome do aluno(a): '))
name2 = str(input('Digite o nome do aluno(a): '))
name3 = str(input('Digite o nome do aluno(a): '))
name4 = str(input('Digite o nome do aluno(a): '))
list = [name1, name2, name3, name4]
shuffle(list)
print("A ordem de apresentação será: {}".format(list))


