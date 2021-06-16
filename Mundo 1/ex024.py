# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
c = str(input('Digite a cidade que você nasceu:  ')).lower()
s = 'santo'
s1 = c.split()
tf = s in s1[0]
if tf:
    print('A cidade começa com "Santo"')
else:
    print('A cidade não começa com "Santo"')
