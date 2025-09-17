"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
num_escolhido = int(input("Escolha um número:\n> "))
for numero in range(1, 11):
    print(f"{num_escolhido} x {numero} = {num_escolhido * numero}")