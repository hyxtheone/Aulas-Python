r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima formam um triângulo ESCALENO')
    elif r1 == r2 and r1 == r3 and r2 == r3:
        print('Os segmentos acima formam um triângulo EQUÍlATERO')
    else:
        print('Os segmentos acima formam um triângulo ISÓSCELES')
else:
    print('Os segmentos acima não formam um triângulo')
