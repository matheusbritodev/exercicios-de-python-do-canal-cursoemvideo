"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""
try:
    nota1 = float(input("Digite a primeira nota:\n> "))
    nota2 = float(input("Digite a segunda nota:\n> "))

    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        media = (nota1 + nota2) / 2
        if media < 5.0: print(f"Sua média é: {media}\nSituação: REPROVADO")
        elif 6.9 >= media >= 5.0: print(f"Sua média é: {media}\nSituação: RECUPERAÇÃO")
        elif media >= 7.0: print(f"Sua média é: {media}\nSituação: APROVADO")
    else:
        print("ERRO: Números acima de 10 e abaixo de 0 não são permitidos.")
except ValueError:
        print("ERRO: Insira apenas números de 0 a 10.")
