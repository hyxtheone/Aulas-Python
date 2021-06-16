# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
d1 = d * 60
km1 = km * 0.15
total = d1 + km1
print(f'O total a pagar é de R${total:.2f}')
