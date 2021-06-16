n = int(input('Digite um número inteiro: '))
print('Você quer converter para:\n[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL')
opção = str(input('Sua opção: '))
if opção == '1':
    b = bin(n)
    print(f'O número {n} convertido para binário é {b[2:]}')
elif opção == '2':
    o = oct(n)
    print(f'O número {n} convertido para octal é {o[2:]}')
elif opção == '3':
    h = hex(n)
    print(f'O número {n} convertido para hexadecimal é {h[2:]}')
else:
    print('Opção inválida!')
