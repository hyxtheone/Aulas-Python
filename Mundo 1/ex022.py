n = str(input('Digite seu nome completo: '))
nma = n.upper()
nmi = n.lower()
nt = len(n.replace(' ', ''))
np = n.split()
print('Analisando seu nome...')
print(f"""Seu nome em letras maiúsculas é {nma}
Seu nome em letras minúsculas é {nmi}
Seu nome tem ao todo {nt} letras
Seu primeiro nome é {np[0]} e tem {len(np[0])} letras""")
