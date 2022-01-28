cont = 0
total = 0
cont2 = 0
menor_preço = 0
mais_barato = ''

while True:

    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$'))
    cont2 = cont2 + 1

    total = total + preço

    if cont2 == 1 or preço < menor_preço:
        menor_preço = preço
        mais_barato = nome

    if preço > 1000:
        cont = cont + 1
    
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ' )).strip().lower()[0]
    if continuar == 'n':
        break

print(f'O valor total é de: R${total:.2f}\n{cont} produtos custam mais de R$1000\n O produto mais barato é o {mais_barato} que custa {menor_preço}')
