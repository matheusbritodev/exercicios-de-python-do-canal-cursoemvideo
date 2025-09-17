"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
total = []
impar = []
par = []
while True:
    num = int(input("Digite um número: "))
    total.append(num)
    par.append(num) if num % 2 == 0 else impar.append(num)
    resposta = str(input("Deseja continuar?"))
    while resposta[0] not in "sn":
        resposta = str(input("Deseja continuar?")).lower()
    if resposta[0] == "n":
        print("Programa finalizado!")
        break
print(f"TOTAL: {total}\nNÚMEROS PARES: {par}\nNÚMEROS ÍMPARES: {impar}\n")
