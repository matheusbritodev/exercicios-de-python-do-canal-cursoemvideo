#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15%de aumento.
#==========================================================

wage = float(input('Qual o salário do funcionário? R$'))
newWage = wage + (wage * 15 / 100)
print('Parabéns, seu salário de R${:.2f} foi reajustado em 15%, agora você vai receber R${:.2f} a partir do próximo mês!'.format(wage, newWage))