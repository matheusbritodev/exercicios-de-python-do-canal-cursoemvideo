"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%.
"""
#==========================================================
salario = float(input('Qual o salário do fúncionário?'))
if salario <= 1250:
    salario += (salario * 0.10)
else:
    salario += (salario * 0.15)
print('O salário do funcionário após o aumento é: R${:.2f}'.format(salario))
