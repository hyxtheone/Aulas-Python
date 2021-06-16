# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto? R$ '))
v = 5 * p / 100
r = p - v
print(f'O produto que custava R${p}, na promoção com desconto de 5% vai custar R${r:.2f} ')

