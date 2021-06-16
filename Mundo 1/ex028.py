from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 10, tente adivinhar')
print('-=-' * 20)
sleep(1)
rn = randint(0, 10)
r = int(input('Tente adivinhar o número que eu pensei: '))
print('PROCESSANDO...')
sleep(2)
if r == rn:
    print('Parabéns!! Você acertou!')
else:
    print(f'Você errou :( eu pensei no número {rn}')
