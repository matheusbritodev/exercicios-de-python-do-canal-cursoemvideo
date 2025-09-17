"""
Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                  
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []

while True:
    i = 0
    num = int(input("Digite um numero: "))
    # Lógica do método sort()
    if i == 0 or num > lista[-1]:
        lista.insert(i, num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
    confirm = str(input("Quer continuar? [S/N]")).lower()
    while confirm[0] not in "sn":
        confirm = str(input("Quer continuar? [S/N]")).lower()
    if confirm[0] == "n":
        break
lista = lista[::-1]
print(f"\nLISTA DE VALORES DESCRESCENTE: {lista}")
print(f"QUANTIDADE DE NÚMEROS DIGITADOS: {len(lista)}")
print(f"O valor 5 não foi digitado" if 5 not in lista else f"O valor 5 foi digitado e está na posição {lista.index(5)}")