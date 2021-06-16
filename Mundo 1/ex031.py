# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,
# 50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input('Qual a distância da viagem? '))
d1 = d * 0.50
d2 = d * 0.45
print(f'Você está prestes a começar sua viagem de {d:.2f}km')
if d <= 200:
    print(f'O preço da sua passagem é de R${d1:.2f}')
else:
    print(f'O preço da sua passagem é de R${d2:.2f}')
