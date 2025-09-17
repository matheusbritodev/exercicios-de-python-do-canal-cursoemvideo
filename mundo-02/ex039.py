'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

ano_de_nascimento = int(input("Digite o ano de seu nascimento\n> "))
idade_para_alistar = 18

ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_de_nascimento
ano_alistar = ano_atual - (idade - idade_para_alistar)
tempo_alistado = idade - idade_para_alistar

if idade > idade_para_alistar:
    print(f"Você tem {idade} anos. Você deveria ter se alistado no ano de {ano_alistar}. seu alistamento foi há {tempo_alistado} anos")
if idade < idade_para_alistar:
    print(f"Você tem {idade} anos. Você vai se alistar no ano de {ano_alistar}.")
if idade == idade_para_alistar:
    print(f"Você tem {idade} anos. Você vai se alistar este ano: {ano_alistar}")
