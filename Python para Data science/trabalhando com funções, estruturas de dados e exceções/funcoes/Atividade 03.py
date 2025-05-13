'''
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
Utilize o return na função e salve a nova lista na variável mult_3.
'''

list_atv2 = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def mult_3(lista):
  multplicados = []
  for numero in lista:
    if numero % 3 == 0:
      multplicados.append(numero)
  return multplicados

multplicados = mult_3(list_atv2)
print(multplicados)