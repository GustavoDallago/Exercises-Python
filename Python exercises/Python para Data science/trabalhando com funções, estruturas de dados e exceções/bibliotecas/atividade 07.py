##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

'''
Você recebeu um desafio de calcular a raiz quadrada de uma lista de números,
identificando quais resultaram em um número inteiro. A lista é a seguinte:
'''

numeros = [2, 8, 15, 23, 91, 112, 256]

for numero in numeros:
  raiz_qdr = math.sqrt(numero)
  if raiz_qdr.is_integer():
    print(f'Raiz quadrada de {numero}: {raiz_qdr} é inteiro')
  else:
    print(f'Raiz quadrada de {numero}: {raiz_qdr}')