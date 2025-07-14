"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai paga.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from math import ceil

#Coleta de dados
valor_da_casa = float(input("Qual o valor da casa?\n> "))
salario_do_cliente = float(input("Qual o salário do comprador?\n> "))
tempo_financiamento = int(input("Quantos anos de financiamento?\n>"))

#Valor da prestação sem juros
prestacao_financiamento = valor_da_casa / (tempo_financiamento * 12)

#Cálculo de taxa de juros mensal
prestacao_com_juros = prestacao_financiamento * 1.21 # taxa: 14.52% a.a.

#Para calcular o salário ideal, o valor da prestação com juros foi dividido por 0.3 para se aproximar do salário ideal e a função ceil() serviu para arredondar o valor para cima, dessa forma os requesitos sempre serão cumpridos.
salario_necessario = ceil(prestacao_com_juros / 0.3)

#Condição para APROVAR ou NEGAR um empréstimo
if prestacao_com_juros > (salario_do_cliente * 0.3): #A regra é que se a prestção for maior que 30% do salário do cliente o empréstimo será NEGADO.
    print(f"Para pagar uma casa de {valor_da_casa:,.2f} em {tempo_financiamento} anos a prestação será de R$ {prestacao_com_juros:,.2f}\n🔴 EMPRÉSTIMO NEGADO!\nSalário ideal para aprovação do financiamento desta casa no período de {tempo_financiamento} anos: R$ {salario_necessario:,.2f}") 
else:
    print(f"Para pagar uma casa de {valor_da_casa:,.2f} em {tempo_financiamento} anos a prestação será de R$ {prestacao_com_juros:,.2f}\n✅ EMPRÉSTIMO APROVADO!")
