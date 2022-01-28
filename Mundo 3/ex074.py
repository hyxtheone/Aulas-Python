from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram {numeros}\nSendo o menor número {min(numeros)} o maior número {max(numeros)}')