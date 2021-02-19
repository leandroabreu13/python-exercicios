# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
valor = int(input('Qual valor a ser sacado? '))
total = valor
ced = 50
total_ced = 0
while True:
  if total >= ced:
    total -= ced
    total_ced += 1
  else:
    if total_ced > 0:
      print(f'Total de {total_ced} cédulas de R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    total_ced = 0
    if total == 0:
      break
print('Volte sempre! Tenha um bom dia')

# 124
# print(valor // 50)         -> 2
# print(valor / 50)          -> 2.48
# print(valor % 50)          -> 24