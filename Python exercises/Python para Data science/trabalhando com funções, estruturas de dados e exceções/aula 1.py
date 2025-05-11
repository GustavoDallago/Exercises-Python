#Made using google colab

!pip install matplotlib==3.7.1
import numpy as np
from random  import choice, randrange
import math

# atividade 3 - Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

random.choice(lista)

# atividade 4 - Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.

random.randrange(1, 100)

# atividade 5 - Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
math.pow(n1,n2)

# atividade 6 - Um programa deve ser escrito para sortear uma pessoa seguidora 
# de uma rede social para ganhar um prêmio. A lista de participantes é numerada e
# devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. 
# Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

qtd_pessoas = int(input('Digite a quantidade de participantes: '))
random.randrange(1, qtd_pessoas)

'''
atividade 7 -

Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. 
O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à 
pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
'''

token = random.randrange(1000, 9998)
nome = input('Digite seu nome: ')

print(f'Olá {nome}, seu token é {token}')


'''
atividade 8 -

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

'''
atividade 9 -

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

'''
atividade 10 -

Faça um programa para uma loja que vende grama para jardins. 
Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. 
Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
'''

math.pi

raio = int(input('Insira o raio da área do seu jardim: '))
area = math.pi * math.pow(raio,2)
valor = area * 25

print(f'Para fazer o seu jardim será necessário R${valor:.2f} em grama')
