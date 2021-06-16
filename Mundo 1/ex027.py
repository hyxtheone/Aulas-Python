# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
n = str(input('Digite seu nome completo: ')).strip()
split = n.split()
len1 = len(split)
print(f'Seu primeiro nome é {split[0]}')
print(f'Seu último nome é {split[len1 - 1]}')
