# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual o salário do funcionário?: R$'))
p = 15 * s / 100
t = s + p
print(f'O funcionário que recebia {s}, com 15% de aumento, passa a receber R${t:.2f}')