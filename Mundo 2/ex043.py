a = float(input('Digite sua altura (m): '))
p = float(input('Digite seu peso (kg): '))
imc = p / (a * a)
print('Você está em', end=' ')
print(f'o IMC é {imc:.2f}')
if imc < 18.4:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 24.9:
    print('Peso ideal')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30 and imc < 39.9:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
