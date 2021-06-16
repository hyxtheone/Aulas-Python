# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
n = int(input('Qual o ano de seu nascimento? '))
i = 2021 - n
print(f'Quem nasceu em {n} tem {i} anos em 2021!')
if i < 18:
    a = 18 - i
    print(f'Ainda faltam {a} anos para seu alistamento!')
    al = a + 2021
    print(f'Seu alistamento será no ano de {al}!')
elif i > 18:
    a = i - 18
    print(f'Você deveria ter se alistado há {a} anos')
    al = 2021 - a
    print(f'Seu alistamento foi no ano de {al}!')
else:
    print('Você precisa se alistar IMEDIATAMENTE!')
