#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#==========================================================

num = int(input('Digite um número:'))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

#Aqui estão 2 alternativas de concatenação na linguagem python

#Alternativa 1
#print('O dobro de ', num, 'vale: ', dobro, '\nO triplo de ', num, 'vale: ', triplo, '\nA raiz quadrada de ', num, 'é igual a: ', raiz)

#Alternativa 2
print('O dobro de {} vale: {} \nO triplo de {} vale: {} \nA raiz quadrada de {} é igual a: {:.2f}'.format(num, dobro, num, triplo, num, raiz))
