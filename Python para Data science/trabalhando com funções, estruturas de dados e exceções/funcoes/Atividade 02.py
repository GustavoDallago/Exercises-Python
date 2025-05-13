'''
Escreva uma função que gere a tabuada de um número inteiro de 1 a 10,
de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7
'''

numero_user = int(input('Digite um numero: '))

print(f'Tabuada do {numero_user}')

for i in range(1, 11):
  print(f'{numero_user} x {i} = {numero_user * i}')