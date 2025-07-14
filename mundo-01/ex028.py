"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deve escrever na tela se o usuário venceu ou perdeu.
"""
#==========================================================
import random
numUser = int(input("Digite um número inteiro entre '0' e '5': "))
numChoice = random.randint(0, 5)
print("You win, congratulations!" if numUser == numChoice else "You Lose, the number choiced was {}".format(numChoice))