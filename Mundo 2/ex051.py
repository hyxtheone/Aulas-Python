p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = p1 + 10 * r
for i in range(p1, f, r):
    print(f'{i}', end=' -> ')
print('Acabou')
