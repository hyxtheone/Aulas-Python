from random import randint

cont = 0

while True:

    numero_robo = randint(1,10)
    escolha = str(input('Par ou impar? (P/I): ')).lower()
    numero_pessoa = int(input('Digite um número: '))

    soma = numero_pessoa + numero_robo
    print(f'Você jogou {numero_pessoa} e o computador jogou {numero_robo}, total {soma}')

    if soma % 2 == 0:
        print('O resultado foi PAR!')
        if escolha == 'p':
            print('Você venceu!')
            cont = cont + 1
        elif escolha == 'i':
            print('Você perdeu! :( ')
            print(f'Foram {cont} acertos consecutivos')
            break
    else:
        print('O resultado foi ÍMPAR!')
        if escolha == 'i':
            print('Você venceu!')
            cont = cont + 1
        elif escolha == 'p':
            print('Você perdeu! :( ')
            print(f'Foram {cont} acertos consecutivos')
            break
