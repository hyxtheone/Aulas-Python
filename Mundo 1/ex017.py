# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.
from math import hypot
o = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacente: '))
h = hypot(o, a)
print(f'A hipotenusa vai medir {h:.2f}')
