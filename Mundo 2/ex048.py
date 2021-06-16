n = 0
r = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        n += i
        r += 1
print(f'A soma de {r} números solicitados é {n}.')
