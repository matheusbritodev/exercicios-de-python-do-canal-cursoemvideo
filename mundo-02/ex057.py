"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = " "
while sexo not in "mf":
    sexo = str(input("Digite qual o seu sexo: (M/F)\n> ")).lower().strip()[0]
    if sexo not in "mf":
        print("Opção inválida! Digite novamente.")
    else:
        print("Você é do sexo MASCULINO") if sexo == "m" else print("Você é do sexo FEMININO")

