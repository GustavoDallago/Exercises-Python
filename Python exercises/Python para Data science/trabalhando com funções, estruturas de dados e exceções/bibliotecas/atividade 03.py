##!pip install matplotlib==3.7.1

import numpy as np
from random  import choice, randrange
import math

# atividade 5 - Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
math.pow(n1,n2)