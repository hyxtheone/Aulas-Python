import random
from time import sleep
print('Suas opções:\n'
      '[ 1 ] Pedra\n'
      '[ 2 ] Papel\n'
      '[ 3 ] Tesoura\n')
o = int(input('Selecione uma opção: '))
r = random.randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
if r == o:
    print('Empate!')
elif o == 1 and r == 2:
    print('O computador venceu, ele jogou PAPEL')
elif o == 2 and r == 3:
    print('O computador venceu, ele jogou TESOURA')
elif o == 2 and r == 1:
    print('O jogador venceu, o computador jogou PEDRA')
elif o == 3 and r == 2:
    print('O jogador venceu, o computador jogou PAPEL')
elif o == 1 and r == 3:
    print('O jogador venceu, o computador jogou TESOURA')
elif o == 3 and r == 1:
    print('O computador venceu, ele jogou PEDRA')
else:
    print('Opção inválida!')
