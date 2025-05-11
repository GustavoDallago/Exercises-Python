from datetime import date

def idade():
    ano = date.today().year
    ano_nasc = int(input('Insira o ano que você nasceu: '))
    idade_atual = ano - ano_nasc
    print(f'A idade é {idade_atual}')

idade()
