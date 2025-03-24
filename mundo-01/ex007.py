#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.
#==========================================================

#Neste exercício vamos descobrir a média de um aluno, para isso vou utilizar o sistema de notas da minha faculdade (UNDB).
print('- A AVQUALIS é uma nota qualitativa que vale até 4.0\n- A P1 e P2 são notas de provas que valem até 6.0 cada uma\n\nA soma dessas 2 notas juntas somarão a nota máxima de 10, essa nota\né dada na N1 (que é feita no primeiro bimestre) e a N2 segue a mesma lógica, mas é a nota do segundo bimestre \n')
name = (input('Qual o nome do aluno?'))

#1 Bimestre
avQualis1 = float(input('Digite uma nota da AVQUALIS1: '))
p1 = float(input('Digite uma nota da P1: '))
n1 = avQualis1 + p1

#2 Bimestre
avQualis2 = float(input('Digite uma nota DA AVQUALIS2: '))
p2 = float(input('Digite uma nota da P2: '))
n2 = avQualis2 + p2

#Média do período
media = (n1 + n2) / 2
print('A média final do aluno {} é de {:.1f}: '.format(name, media))

