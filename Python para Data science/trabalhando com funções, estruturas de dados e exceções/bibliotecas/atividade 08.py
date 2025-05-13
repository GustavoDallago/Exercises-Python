##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

'''
Faça um programa para uma loja que vende grama para jardins.
Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00.
Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
'''

math.pi

raio = int(input('Insira o raio da área do seu jardim: '))
area = math.pi * math.pow(raio,2)
valor = area * 25

print(f'Para fazer o seu jardim será necessário R${valor:.2f} em grama')