"""
Exercício Python 089: 
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
#LISTAS
lista_alunos = []

# LOOP PARA ADICIONAR UM NOVO ALUNO E SUAS RESPECTIVAS NOTAS
while True:
    # COLETA DE DADOS
    nome_aluno_adicionar = input("Nome:\n> ")
    try:
        nota1 = float(input(f"Digite a primeira nota do aluno {nome_aluno_adicionar}:\n> "))
        nota2 = float(input(f"Digite a segunda nota do aluno {nome_aluno_adicionar}:\n> "))
    except ValueError:
        print("ERRO: Por favor, digite um número para a nota!")
        continue

    # VERIFICA SE O NOME DO ALUNO JÁ EXISTE NA LISTA ANTES DE ADICIONAR
    nome_encontrado = False
    for aluno in lista_alunos:
        if aluno[0] == nome_aluno_adicionar:
            nome_encontrado = True
            break
    if nome_encontrado == True:
        print("Este aluno já existe na lista.") # SE O NOME JÁ EXISTIR ELE VAI ALERTAR O USUÁRIO
    else:
        lista_alunos.append([nome_aluno_adicionar, [nota1, nota2]])

    # SOLICITA CONFIRMAÇÃO DO USUÁRIO SE DESEJA CONTINUAR A ADICIONAR NOVOS DADOS OU NÃO
    while True:
        confirmacao_continuar = input("Deseja continuar? [S/N]\n> ").lower()
        if confirmacao_continuar == "s" or confirmacao_continuar == "n":
            break
        print("ERRO: Opcão inválida! Digite apenas 's' ou 'n'.")
    if confirmacao_continuar == "n":
        break

# EXIBIÇÃO DO BOLETIM
print(f"{"-=" * 16}\n{"No.".center(4)}|{"Nome.".center(15)}|{"Média".center(12)}\n{"-" * 32}")
for indice, aluno in enumerate(lista_alunos):
    # CALCULO DA MÉDIA
    media = (aluno[1][0] + aluno[1][1]) / len(aluno[1])
    lista_alunos[indice].append(media)
    print(f"{str(indice).center(4)}|{aluno[0].center(15)}|{str(f"{lista_alunos[indice][2]:.1f}").center(12)}\n")
    print(f"{"-" * 32}")
    print(indice, aluno)

# LOOP PARA VISUALIZAR AS NOTAS INDIVIDUAIS
while True:
    choice = int(input("Digite o indice do aluno para ver as notas: (999 interrompe)\n> "))
    if choice == 999: 
        break
    else:
        print(f"Notas de {lista_alunos[choice][0]} são {lista_alunos[choice][1]}\n{"-" * 32}")