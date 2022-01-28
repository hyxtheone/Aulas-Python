numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

input_numero = int(input('Digite um número de 0 a 20: '))

while True:

    if input_numero < 0:
        input_numero = int(input('Tente novamente, digite um número de 0 a 20: '))
    elif input_numero > 20:
        input_numero = int(input('Tente novamente, digite um número de 0 a 20: '))
    else:
        break

print(f'Você digitou o número {numeros_extenso[input_numero]}')