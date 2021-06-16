f = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A apareceu {f.count("a")} vezes na frase')
print(f'A primeira letra A apareceu na posição {f.find("a")+1}')
print(f'A ultima letra A apareceu na posição {f.rfind("a")+1}')
