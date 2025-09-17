"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
"""

lista = []

resp = "ns"
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Esse número já está na lista")
    resp = str(input("Deseja continuar? [S/N]")).lower()
    if resp == "n": break
    elif resp == "s": continue
    else: 
        print("Opção inválida! Tente novamente.")
        continue
print(sorted(lista))