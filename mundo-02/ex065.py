"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
maior, menor, cont, soma, media = 0, 0, 0, 0, 0 
resp = "s"
while resp in "Ss":
    num = int(input("Digite um número:\n> "))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if menor > num: menor = num
        if maior < num: maior = num
    resp = str(input("Deseja continuar: [S/N]\n> "))
media = soma / cont
print(f"Você digitou {cont} números e a média foi {media}\nO maior valor foi {maior} e o menor foi {menor}")