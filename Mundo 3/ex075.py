cont = 0

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
numero4 = int(input('Digite o último número: '))

tupla = (numero1, numero2, numero3, numero4)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')

for i in tupla:
    if i % 2 == 0:
        cont = cont + 1

if 3 in tupla:
    numero_tres = tupla.index(3)
    print(f'O valor 3 apareceu na {numero_tres + 1}° posição')
else:
    print('O valor 3 não foi digitado')

if cont > 0:
    print(f'Os valores pares digitados foram:', end=' ')
else:
    print('Não foram digitados valores pares')

for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')