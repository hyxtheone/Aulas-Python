a = int(input('Qual o ano de nascimento? '))
i = 2021 - a
print(f'Você tem {i} anos')
if i <= 9:
    print('Sua categoria é MIRIM')
elif i > 9 and i <= 14:
    print('Sua categoria é INFANTIL')
elif i > 14 and i <= 19:
    print('Sua categoria é JUNIOR')
elif i > 19 and i <= 25:
    print('Sua categoria é SÊNIOR')
elif i > 25:
    print('Sua categoria é MASTER')
