"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
total = [[], []]

for i in range(0, 7):
    n = int(input(f"Digite o {i + 1}o número: "))
    total[0].append(n) if n % 2 == 0 else total[1].append(n)
print(f"Os valore pares digitados foram: {sorted(total[0])}\nOs valore ímpares digitados foram: {sorted(total[1])}")