"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
#EU
from unidecode import unidecode

frase = unidecode(str(input("Digite uma frase para verificar se é um palíndromo:\n> "))).replace(" ", "").upper().strip()
contrario = frase[::-1]
print(f" A frase '{frase}' é um palíndromo!") if frase == contrario else print(f" A frase '{frase}' NÃO é um palíndromo!")

#GUANABARA
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')