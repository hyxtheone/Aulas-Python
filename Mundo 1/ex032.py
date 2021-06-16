# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
import calendar
a = int(input('Qual ano você quer analisar? '))
a1 = calendar.isleap(a)
if a1 is True:
    print('Seu ano é bissexto')
else:
    print('Seu ano não é bissexto')