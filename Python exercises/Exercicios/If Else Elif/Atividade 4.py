#Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o
#IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC 
#e uma mensagem indicando se está abaixo do peso (IMC < 18.5), 
#peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

peso = float(input('Insira o seu peso (KG): '))
altura = float(input('Insira a sua altura (M): '))
IMC = peso / (altura ** 2)

if IMC < 18.5:
  print(f'Seu peso é: {peso}')
  print(f'Sua altura é: {altura}')
  print(f'Seu IMC é {IMC:.2f} e está abaixo do peso')
elif 18.5 <= IMC < 25:
  print(f'Seu peso é: {peso}')
  print(f'Sua altura é: {altura}')
  print(f'Seu IMC é {IMC:.2f} e está no peso normal')
else:
  print(f'Seu peso é: {peso}')
  print(f'Sua altura é: {altura}')
  print(f'Seu IMC é {IMC:.2f} e está acima do peso')