"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num >= 0:
        cont = 1
        while cont < 10:
            print(f"{num} x {cont} = {num * cont}")
            cont += 1
    else:
        print("Programa tabuada finalizado. Volte sempre que precisar!")
        break