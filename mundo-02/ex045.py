"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import randint
from time import sleep


escolha = str(input("Escolha uma das opcões:\n[1] Pedra\n[2] Papel\n[3] Tesoura\n> "))
escolha_oponente = randint(1,3)

if escolha in "123":
    escolha = int(escolha)
    print("\nJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    if escolha == 1:
        if escolha_oponente == 1:
            print("EMPATOU! Seu oponente também escolheu pedra")
        elif escolha_oponente == 3:
            print("VOCÊ VENCEU! Seu oponente escolheu tesoura")
        else:
            print("VOCÊ PERDEU! Seu oponente escolheu papel")
    if escolha == 2:
        if escolha_oponente == 2:
            print("EMPATOU! Seu oponente também escolheu papel")
        elif escolha_oponente == 1:
            print("VOCÊ VENCEU! Seu oponente escolheu pedra")
        else:
            print("VOCÊ PERDEU! Seu oponente escolheu tesoura")
    if escolha == 3:
        if escolha_oponente == 3:
            print("EMPATOU! Seu oponente também escolheu tesoura")
        elif escolha_oponente == 2:
            print("VOCÊ VENCEU! Seu oponente escolheu papel")
        else:
            print("VOCÊ PERDEU! Seu oponente escolheu pedra")
else:
    print("ERRO: Jogada inválida. Escolha apenas um número de 1 a 3 para selecionar uma opção!")