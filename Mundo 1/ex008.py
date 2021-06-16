# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
d = float(input('Digite uma distância em metros: '))
print(f'A medida de {d}m corresponde a:')
print(f'{d / 1000}km')
print(f'{d /100}hm')
print(f'{d / 10}dam')
print(f'{d * 10}dm')
print(f'{d * 100}cm')
print(f'{d * 1000}mm')
