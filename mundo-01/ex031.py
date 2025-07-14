"""
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
"""
#==========================================================
distance = float(input("Quantos km você vai percorrer na sua viagem? "))

if distance <= 200:
    price = distance * 0.50
    print("O valor da sua passagem é R$ {:.2f}".format(price).replace(".", ","))
else:
    price = distance * 0.45
    print("O valor da sua passagem é R$ {:.2f}".format(price).replace(".", ","))