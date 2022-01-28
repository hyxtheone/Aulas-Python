times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

chapecoense = times.index('Chapecoense')

print(f'Os 5 primeiros colocados foram: {times[0:5]}')
print(f'Os 4 ultimos colocados foram: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A chapecoense ficou em: {chapecoense + 1}° Lugar')