#Escreva um programa que converta uma temperatura digitada em ºC para ºF.
#==========================================================
city = input('Qual o nome da sua cidade?')
tempC = float(input('Qual a temperatura ambiente em ºC da cidade {}?'.format(city)))
tempF = tempC * 1.8 + 32
print('A temperatura em {} é de {}ºC, convertido em fahrenheit é de: {}ºF'.format(city, tempC, tempF))