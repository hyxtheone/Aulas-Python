# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
n = float(input('Digite um número: '))
a = floor(n)
print(f'O valor digitado foi de {n} e a sua porção inteira é {a}')
