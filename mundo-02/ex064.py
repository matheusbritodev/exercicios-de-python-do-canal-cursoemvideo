"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
"""
cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input("Digite um úmero [999 para parar]: "))
    if num != 999:
        soma += num
        cont += 1
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")