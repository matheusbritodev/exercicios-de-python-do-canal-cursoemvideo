"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
from time import sleep

cont_mais_18, homens, mulheres_menos_20 = 0, 0, 0

while True:
    idade = int(input("Qual sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F]: ")).lower()
    if idade > 18:
        cont_mais_18 += 1
    if sexo in "m":
        homens += 1
    if idade < 20 and sexo in "f":
        mulheres_menos_20 += 1
    print("Finalizando cadastro...")
    sleep(1)
    print("Novo cadastro concluído com sucesso!")
    continuar = ' '
    while continuar[0] not in "sn":
        continuar = str(input("Quer efetuar outro cadastro [S/N]?")).lower()
    if continuar[0] in "n":
        print("Finalizando programa...")
        sleep(2)
        print("Programa Finalizado. Volte sempre!")
        break
print(f"{"-=" *18}\nUSUÁRIOS COM MAIS DE 18 ANOS: {cont_mais_18}\nMULHERES COM MENOS DE 20 ANOS: {mulheres_menos_20}\nTOTAL DE HOMENS: {homens}\n{"-=" *18}")