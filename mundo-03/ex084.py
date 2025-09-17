"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
"""
total, temp = [], []
maior, menor = 0, 0

while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    temp.append(nome)
    temp.append(peso)
    if len(total) == 0:
        maior, menor = temp[1], temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    total.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N]")).lower()
    while resp not in "sn":
        resp = str(input("Quer continuar? [S/N]")).lower()
    if resp == "n":
        break
print(f"Ao todo você cadastrou {len(total)} pessoas.")
print(f"O maior peso foi de {maior}Kg. O peso de ", end="")
for i in total:
    if i[1] == maior:
        print(f"[{i[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}Kg. ", end="")
for i in total:
    if i[1] == menor:
        print(f"Peso de [{i[0]}] ", end="")
print()