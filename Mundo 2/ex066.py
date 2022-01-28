cont = 0
soma = 0

while True:

    numero = int(input('Digite um número (999 para parar): '))

    if numero == 999:
        break

    soma = soma + numero
    cont = cont + 1

print(f'A soma dos {cont} números digitados é de {soma}')
