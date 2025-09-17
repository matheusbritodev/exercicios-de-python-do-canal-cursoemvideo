"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço normal 

– 3x ou mais no cartão: 20% de juros
"""

preco_produto = float(input("Digite o preço do produto:\n> "))
escolha = int(input("""
Qual o método de pagamento?\n
[1] – à vista dinheiro/cheque: 10% de desconto
[2] – à vista no cartão: 5% de desconto
[3] – em até 2x no cartão: preço normal 
[4] – 3x ou mais no cartão: 20% de juros\n> 
"""))

if escolha == 1:
    desconto = preco_produto * 0.10
    preco_produto = preco_produto - desconto
    print(f"\nDesconto de R$ {desconto:.2f} aplicado com sucesso!\nPreço: R$ {preco_produto:.2f}")
elif escolha == 2:
    desconto = preco_produto * 0.05
    preco_produto = preco_produto - desconto
    print(f"\nDesconto de R$ {desconto:.2f} aplicado com sucesso!\nPreço: R$ {preco_produto:.2f}")
elif escolha == 3:
    print(f"\nPagamento parcelado em 2x s/ juros selecionado com sucesso!\nPreço: R$ {preco_produto:.2f}")
elif escolha == 4:
    quantidade_parcelas = int(input("Quantas parcelas?\n> "))
    juros = preco_produto * 0.20
    preco_produto = preco_produto + juros
    valor_parcelas = preco_produto / quantidade_parcelas
    print(f"\nPagamento parcelado selecionado em {quantidade_parcelas}x de R$ {valor_parcelas:.2f} c/ juros.\nPreço final: R$ {preco_produto:.2f}")
else:
    print("Opção inválida! Escolha uma das opções disponíveis!\n>> [1], [2], [3], [4]")