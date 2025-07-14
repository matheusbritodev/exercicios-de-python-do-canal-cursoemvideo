#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santa"
#==========================================================
cid = input('Qual o nome da cidade que você nasceu?').strip().lower()
print(cid[:5] == "santa")