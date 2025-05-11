#Crie um programa que receba a distância percorrida e informe o valor do 
#pedágio correspondente.

distancia = int(input('Insira a distância percorrida (KM): '))

if distancia <= 100:
  print('Valor de pedágio: R$10,00')
elif 100 < distancia <= 200:
  print('Valor de pedágio: R$20,00')
elif distancia > 200:
  print('Valor de pedágio: R$30,00')