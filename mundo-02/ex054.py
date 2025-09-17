"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

ano_atual = date.today().year
contador_maior = 0
contador_menor = 0

for ano in range(1, 8):
    ano_nascimento = int(input("Digite o ano de nascimento:\n> "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        contador_maior += 1
    else:
        contador_menor += 1
        
print(f"No total {contador_maior} pessoas já atingiram a maioridade e {contador_menor} ainda não atingiram")