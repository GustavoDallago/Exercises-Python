import random

numero_aleatório = random.randint(1,10)

while True:
    numero_jogador = int(input('Insira um numero de 1 a 10: '))
    if numero_jogador == numero_aleatório:
        print(f'Você acertou, o numero era: {numero_aleatório}')
        break

    if numero_jogador > numero_aleatório:
        print('O numero é menor do que o digitado')
    elif numero_jogador < numero_aleatório:
        print('O numero é maior do que o digitado')