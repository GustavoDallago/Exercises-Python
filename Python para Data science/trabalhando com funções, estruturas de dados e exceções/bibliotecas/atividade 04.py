##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

#Um programa deve ser escrito para sortear uma pessoa seguidora
# de uma rede social para ganhar um prêmio. A lista de participantes é numerada e
# devemos escolher aleatoriamente um número de acordo com a quantidade de participantes.
# Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

qtd_pessoas = int(input('Digite a quantidade de participantes: '))
random.randrange(1, qtd_pessoas)