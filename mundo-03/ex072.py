"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

lista = ((1, "um"), (2, "dois"), (3, "três"), (4, "quatro"), (5, "cinco"), (6, "seis"), (7, "sete"), (8, "oito"), (9, "nove"), (10, "dez"), (11, "onze"), (12, "doze"), (13, "treze"), (14, "quatorze"), (15, "quinze"), (16, "dezesseis"), (17, "dezessete"), (18, "dezoito"), (19, "dezenove"), (20, "vinte"))


while True:
    num = int(input("Digite um número de 1 a 20: "))
    if 0 <= num <= 20: 
        for tupla in lista:
            for elemento in tupla:
                if elemento == num:
                    print(lista[elemento - 1][1])
    else:
        print("ERRO: Escolha apenas números entre 1 e 20")
        continue
    continuar = " "
    while continuar not in "sn":
        continuar = str(input("Quer continuar? [S/N]\n> ")).lower()
    if continuar in "n":
            break
print("PROGRAMA FINALIZADO!")   