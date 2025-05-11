numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for numero in numeros:
  if numero % 3 == 0 and numero % 5 == 0:
    print(f'{numero} FizzBuzz')
  elif numero % 5 == 0:
    print(f'{numero} Buzz')
  elif numero % 3 == 0:
    print(f'{numero} Fizz')
  else:
    print(numero)