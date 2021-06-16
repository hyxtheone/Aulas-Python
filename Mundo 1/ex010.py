# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
import requests
v = float(input('Digite quantos reais você tem (Utilize "." ao invés de ","): R$ '))
d = requests.get('https://economia.awesomeapi.com.br/all/BRL-USD')
c = d.json()
dolar = c['BRL']['bid']
r = float(dolar)
total = r * v
print('Data da cotação utilizada no cálculo: ' + c['BRL']['create_date'])
print(f'Com R${v:.2f}, você pode comprar: US${total:.2f}')
