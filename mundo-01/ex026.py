"""
Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "a".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a ultima vez.
"""
#==========================================================
frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra 'a' aparece a primeira vez na posição: ", frase[0:].find("a")+1, 
      "\nA letra 'a' aparece a última vez na posição: ", frase[0:].rfind("a")+1, 
      "\nA letra 'a' apareceu {} vezes na frase".format(frase[0:].count("a")))