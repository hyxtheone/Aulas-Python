from math import floor


valor_sacar = int(input('Digite o valor que deseja sacar: '))

cinquenta = valor_sacar / 50
cinquenta_floor = floor(cinquenta)
valor_sacar = valor_sacar - cinquenta_floor * 50

vinte = valor_sacar / 20
vinte_floor = floor(vinte)
valor_sacar = valor_sacar - vinte_floor * 20

dez = valor_sacar / 10
dez_floor = floor(dez)
valor_sacar = valor_sacar - dez_floor * 10

um = valor_sacar / 1

if cinquenta_floor != 0:
    print(f'Total de cédulas de 50: {cinquenta_floor} ')
if vinte_floor != 0:
    print(f'Total de cédulas de 20: {vinte_floor} ')
if dez_floor != 0:
    print(f'Total de cédulas de 10: {dez_floor} ')
if um != 0:
    print(f'Total de cédulas de 1: {um:.0f} ')
