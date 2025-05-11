import re

Url_validacao = input('Insira uma url: ')

if Url_validacao.startswith('"https://') and Url_validacao.endswith('.com'):
    print('Url válida')
else: 
    print('Url inválida')