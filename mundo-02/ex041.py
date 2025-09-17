"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import datetime

ano_nascimento = int(input("Digite o seu ano de nsacimento:\n> "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9: print(f"O atleta tem {idade} anos\nClassificação: MIRIM")
elif 10 <= idade <= 14: print(f"O atleta tem {idade} anos\nClassificação: INFANTIL")
elif 15 <= idade <= 19: print(f"O atleta tem {idade} anos\nClassificação: JÚNIOR")
elif 20 <= idade <= 25: print(f"O atleta tem {idade} anos\nClassificação: SÊNIOR")
elif idade > 25: print(f"O atleta tem {idade} anos\nClassificação: MASTER")
else: 
    print("Ano de nascimento inválido!")