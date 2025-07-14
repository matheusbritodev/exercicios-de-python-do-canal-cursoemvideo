"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$ 7,00 por cada km acima do limite
"""
#==========================================================
speed = int(input("Digite a velocidade do seu carro em km/h:\nex:55\n"))
if speed > 80:
    diference = speed - 80
    print("Você foi multado! Deve pagar R${:.2f} em até 30 dias.".format(diference * 7))
else:
    print("Tudo bem, você está dentro do limite permitido")