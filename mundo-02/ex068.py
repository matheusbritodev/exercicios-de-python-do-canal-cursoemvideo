"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
from random import randint

computador = randint(1, 10)
vitoria = 0
chance = 3

while True:
    dedos = int(input("Diga um valor de 1 a 10: "))
    par_ou_impar = str(input("Par ou ímpar? [P/I] ")).upper()
    soma_dedos = dedos + computador

    if par_ou_impar in "P":
        if soma_dedos % 2 == 0:
            print(f"O computador jogou {computador} e você jogou {dedos}.\nTotalizando {soma_dedos}, deu par\nVocê venceu")
            vitoria += 1

        else:
            print(f"O computador jogou {computador} e você jogou {dedos}.\nTotalizando {soma_dedos}, deu ímpar\nVocê perdeu")
            chance -= 1

    elif par_ou_impar in "I":
        if soma_dedos % 2 != 0:
            print(f"O computador jogou {computador} e você jogou {dedos}.\nTotalizando {soma_dedos}, deu ímpar\nVocê venceu")
            vitoria += 1

        elif par_ou_impar in "I":
            print(f"O computador jogou {computador} e você jogou {dedos}.\nTotalizando {soma_dedos}, deu par\nVocê perdeu")
            chance -= 1

    else:
        print("Opção inválida! Tente novamente")
    if chance == 0: break

print(f"GAME OVER!\nVocê venceu {vitoria} vezes.")