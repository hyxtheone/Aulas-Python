while True:

    numero_tabuada = int(input('Digite um número que você quer ver a tabúada: '))

    print('-' * 20)

    if numero_tabuada < 0:
        break

    for i in range(1, 11):
        print(f'{numero_tabuada} x {i} = {numero_tabuada * i}')
    
    print('-' * 20)
