# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)
print(f' O ângulo de {a} tem o SENO de {s:.2f}\n O ângulo de {a} tem o COSSENO de {c:.2f}\n O ângulo de {a} tem o '
      f'TANGENTE de {t:.2f}')
