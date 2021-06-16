# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
me = (n1 + n2) / 2
if me >= 7:
    print(f'Sua média foi {me}')
    print('Você foi APROVADO!')
elif me >= 5 and me <= 6.9:
    print(f'Sua média foi {me}')
    print('Você está de RECUPERAÇÃO')
elif me < 5:
    print(f'Sua média foi {me}')
    print('Você está REPROVADO!')
