##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

'''
Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso
em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente
3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente.
Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
'''

frutas = ["maçã", "banana", "uva", "pêra",
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

item = random.sample(frutas, 3)

print('Salada de frutas surpresa: ')
for fruta in item:
  print(fruta)