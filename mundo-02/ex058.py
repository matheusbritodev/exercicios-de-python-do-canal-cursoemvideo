"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint

palpites = 0
num_aleatorio = randint(1, 10)
escolha = 0

while escolha != num_aleatorio:
    escolha = int(input("Digite um número de 1 a 10:\n> "))
    if escolha == num_aleatorio:
        print(f"PARABÉNS VOCÊ ACERTOU!\nO número aleatório era {num_aleatorio}. Você precisou de {palpites + 1} palpites.") 
    else:
        if escolha > num_aleatorio:
            print("Menos... Tente mais uma vez.")
            palpites += 1
        elif escolha < num_aleatorio:
            print("Mais... Tente mais uma vez.")
            palpites += 1