#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
#==========================================================

price = float(input('Qual o preço do produto? R$'))
newPrice = price - (price * 5) / 100
print('O produto custa R${:.2f}, na promoção com desconto de 5% ele passa a custar R${:.2f}'.format(price, newPrice))
