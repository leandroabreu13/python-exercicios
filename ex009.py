# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
print('{} * 1 = {}'.format(numero, numero * 1))
print('{} * 2 = {}'.format(numero, numero * 2))
print('{} * 3 = {}'.format(numero, numero * 3))
print('{} * 4 = {}'.format(numero, numero * 4))
print('{} * 5 = {}'.format(numero, numero * 5))
print('{} * {:2} = {}'.format(numero, 6, numero * 6))
print('{} * {:2} = {}'.format(numero, 7, numero * 7))
print('{} * {:2} = {}'.format(numero, 8, numero * 8))
print('{} * {:2} = {}'.format(numero, 9, numero * 9))
print('{} * {} = {}'.format(numero, 10, numero * 10)) 
print('-' * 12)