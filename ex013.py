# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = int(input('Digite seu salário atual:R$ '))
novo_salario = salario + salario * 0.15
print('Seu novo salário é R${:.2f}'.format(novo_salario))