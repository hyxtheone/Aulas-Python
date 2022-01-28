palavras = ('carro', 'aviao', 'homem', 'trabalhar', 'programar')

vogais = ('a', 'e', 'i', 'o', 'u')

for i in palavras:
    print(f'Na palavra {i} temos as vogais', end=' ')

    for v in vogais:
        
        if v in i:
            print(v, end=' ')

    print('')