#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#==========================================================

cash = float(input('Quanto dinheiro você tem na carteira?'))
convert = cash / 5.73
print('Com R${} você pode comprar U${:.2f}'.format(cash, convert))

#Cotação do dólar no dia 24/03/2025 --> R$5.73