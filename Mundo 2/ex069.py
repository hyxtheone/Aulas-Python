cont_idade = 0
cont_homem = 0
cont_mulher = 0

while True:

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]

    if idade > 18:
        cont_idade = cont_idade + 1

    if sexo == 'm':
        cont_homem = cont_homem + 1

    if sexo == 'f' and idade < 20:
        cont_mulher = cont_mulher + 1

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]


    if continuar == 'n':
        print('Programa finalizado.')
        break

print(f'Total de pessoas com mais de 18 anos: {cont_idade}\nTotal de homens cadastrados: {cont_homem}\nTotal de mulher com menos de 20 anos: {cont_mulher}')