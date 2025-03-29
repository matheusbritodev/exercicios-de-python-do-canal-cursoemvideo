#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#==========================================================

km = float(input('Qual a quantidade de km percorrido?'))
days = int(input('Por qunatos dias o veículo foi alugado?'))
priceToPay = (60 * days) + (km * 0.15)

print('O preço total a pagar pelo aluguel do carro é: R${:.2f}'.format(priceToPay))