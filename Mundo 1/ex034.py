# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Digite o salário do funcionário: '))
if s > 1250.00:
    p = 10 * s / 100
else:
    p = 15 * s / 100
r = s + p
print(f'Quem ganhava R${s:.2f}, passa a receber R${r:.2f}')
