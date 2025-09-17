"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

peso = float(input("Digite seu peso:\n> "))
altura = float(input("Digite sua altura:\n> "))
imc =  peso / (altura * altura)

if imc < 18.5: print(F"Peso: {peso}KG\nAltura: {altura}M\nIMC: {imc:.2F}\nSituação: ABAIXO DO PESO")
elif 18.5 <= imc <= 24.9 : print(F"Peso: {peso}KG\nAltura: {altura}M\nIMC: {imc:.2F}\nSituação: PESO IDEAL")
elif 25 < imc <= 29.9: print(F"Peso: {peso}KG\nAltura: {altura}M\nIMC: {imc:.2F}\nSituação: SOBREPESO")
elif 30 < imc <= 39.9: print(F"Peso: {peso}KG\nAltura: {altura}M\nIMC: {imc:.2F}\nSituação: OBESIDADE")
elif imc > 40: print(F"Peso: {peso}KG\nAltura: {altura}M\nIMC: {imc:.2F}\nSituação: OBESIDADE MÓRBIDA")
