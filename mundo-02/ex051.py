"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

termo = int(input("Digite o primeiro termo:\n> "))
razao = int(input("Digite a razão:\n> "))
pa = termo + (10 - 1) * razao

for i in range(termo, pa + razao, razao):
    print(i, end=" --> ")