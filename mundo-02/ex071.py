"""
Crie umm programa ue simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor sacado (número inteiro) de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$5, R$2 e R$1.
"""
valor_sacado = int(input("Digite o valor que deseja sacar: "))
total = valor_sacado
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if total > 0:
            print(f"Total de {totced} cedulas de R${ced:.2f}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        if total == 0:
            break
print("Programa finalizado!")



"""cedulas = [50, 20, 10, 5, 2, 1]

valor_saque = int(input("Qual valor você deseja sacar? R$ "))

print("\n===================================================")
print(f"Para sacar o valor de R$ {valor_saque:.2f} você receberá:")
print("===================================================")

for cedula in cedulas:
    quantidade_cedulas = valor_saque // cedula
    if quantidade_cedulas > 0:
        print(f"{quantidade_cedulas} cédula(s) de R$ {cedula}")
        valor_saque %= cedula

print("===================================================")
"""
























