"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = int(input("Digite um número:\n> "))
num2 = int(input("Digite outro número:\n> "))

maior_num = 0
escolha = 0

while escolha != 5:
    escolha = int(input("""
Digite uma opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
>> """))

    if escolha == 1: print(f"{num1} + {num2} = {num1 + num2}")
    elif escolha == 2: print(f"{num1} x {num2} = {num1 * num2}")
    elif escolha == 3:
        if num1 > maior_num: maior_num = num1
        if num2 > maior_num: maior_num = num2
        print(f"Maior número: {maior_num}")
    elif escolha == 4:
        num1 = int(input("Digite um número:\n> "))
        num2 = int(input("Digite outro número:\n> "))
        print(f"Número atualizados com sucesso!\nSeus novos números são {num1} e {num2} respectivamente.")
    elif escolha == 5:
        confirm = str(input("Tem certeza que deseja sair? (S/N)\n>")).lower()
        if confirm[0] == "s": 
            print("Finalizando...")
            sleep(2)
        if confirm[0] == "n": continue
    else:
        print("Opção inválida! Tente novamente.")
print("Programa finalizado! Volte sempre!")
