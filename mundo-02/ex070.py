"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
produtos_mil_reais, total, produto_mais_barato, nome_produto = 0, 0, 0, ""
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    total += preco
    if preco > 1000: produtos_mil_reais += 1
    if produto_mais_barato == 0:
        produto_mais_barato = preco
        nome_produto = produto
    else:
        if produto_mais_barato > preco:
            produto_mais_barato = preco
            nome_produto = produto
    continuar = " "
    while continuar[0] not in "sn":
        continuar = str(input("Quer continuar? ")).lower()
    if continuar[0] in "n":
        break
print(f"TOTAL DA COMPRA: R${total:.2f}\nQUANTIDADE DE PRODUTOS QUE CUSTAM MAIS DE MIL REAIS: {produtos_mil_reais}\nPRODUTO MAIS BARATO: {nome_produto}\nPREÇO DO PRODUTO MAIS BARATO: R${produto_mais_barato:2f}")