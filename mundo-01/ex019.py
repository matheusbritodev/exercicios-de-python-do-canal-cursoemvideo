#Um professor quer sortear um dos seus 8 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
#==========================================================

from random import choice
list = ["Mateus Raposo","Matheus Brito", "Carlos Silva","Ana Paula","Pedro Lucas","Vinícius Oliveira","Rômulo","Hector"]
new_list = choice(list)
print("O aluno escolhido é: {}".format(new_list))


#Método do Guanabara
"""
name1 = str(input("Primeiro aluno: "))
name2 = str(input("Primeiro aluno: "))
name3 = str(input("Primeiro aluno: "))
name4 = str(input("Primeiro aluno: "))
lista = [name1, name2, name3, name4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.formaat(escolhido))
"""