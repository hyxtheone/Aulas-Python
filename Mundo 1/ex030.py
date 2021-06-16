#  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
n = n % 2
if n == 0:
    print('O seu número é PAR!')
else:
    print('O seu número é ÍMPAR!')
