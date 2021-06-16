# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
km1 = int(input('Qual é a velocidade atual do carro? '))
if km1 > 80:
    r = (km1 - 80) * 7
    print(f'Você foi multado por exceder o limite de velocidade de 80km/h! Você terá que pagar o valor total de R${r}.00 ')
print('Tenha um bom dia! Dirija com segurança!')
