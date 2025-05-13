##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

'''
Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa.
O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à
pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
'''

token = random.randrange(1000, 9998)
nome = input('Digite seu nome: ')

print(f'Olá {nome}, seu token é {token}')
