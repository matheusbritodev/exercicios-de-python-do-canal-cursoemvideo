"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
idade_soma = 0
idade_homem_mais_velho = 0
cont_mulher_menos20 = 0

for i in range(1, 5):
    nome = str(input(f"Digite o nome da {i}ª pessoa:\n> "))
    sexo = str(input(f"Digite o sexo da {i}ª pessoa: (M/F)\n> ")).lower()
    idade = int(input(f"Digite o idade da {i}ª pessoa:\n> "))
    idade_soma += idade
    if sexo == "m" and idade_homem_mais_velho < idade:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo == "f" and idade < 20:
        cont_mulher_menos20 += 1

media = idade_soma / i
print(f"A média de idade do grupo é: {media:.2f} anos\nO homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}\nO grupo tem {cont_mulher_menos20} mulher(es) com menos de 20 anos.")
