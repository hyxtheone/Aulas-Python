# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
v = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
f = int(input('Quantos anos de financiamento? '))
po = s * 30 / 100
p2 = v / f / 12
print(f'Para pagar uma casa de R${v:.2f} em {f} anos de prestação será de R${p2:.2f}')
if po >= p2:
    print('Empréstimo aceito!')
else:
    print('Empréstimo negado!')
