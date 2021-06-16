from time import sleep
pr = float(input('Digite o valor comprado: R$'))
print('[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão\n')
f = input('Escolha uma opção: ')
print('Processando...')
sleep(1)
while True:
    if f == '1':
        d = pr * 10 / 100
        d = pr - d
        print(f'Sua compra de R${pr:.2f} vai custar R${d:.2f} no final.')
        break
    elif f == '2':
        d = pr * 5 / 100
        d = pr - d
        print(f'Sua compra de R${pr:.2f} vai custar R${d:.2f} no final.')
        break
    elif f == '3':
        print(f'O valor final da compra será de R${pr:.2f}')
        break
    elif f == '4':
        pa = int(input('São em quantas parcelas? '))
        if pa >= 3:
            print('Calculando...')
            sleep(1)
            j = pr * 20 / 100
            ju = pr + j
            print(f'Sua compra parcelada em {pa}x terá um juros de R${j:.2f}')
            print(f'O valor final será R${ju:.2f}')
            break
        else:
            print('Valor inválido! Digite novamente.')
            continue
