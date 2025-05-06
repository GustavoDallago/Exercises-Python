import re

receita = input('Insira uma receita médica: ')
numero = re.findall(r'\d+', receita)[0]

print(f'O numero da sua receita é: {numero}')