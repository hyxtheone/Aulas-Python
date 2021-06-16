# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
n = str(input('Digite seu nome completo: ')).lower()
s = 'silva'
s1 = n.split()
tf = s in s1
if tf:
    print('Seu nome tem Silva? Sim')
else:
    print('Seu nome tem Silva? Não')
