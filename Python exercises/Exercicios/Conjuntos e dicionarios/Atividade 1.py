convidados = set()

while True:
    nome = input('Insira o nome do convidado (ou digite "sair"): ')
    if nome.lower() == 'sair':
        break
    convidados.add(nome)
print(convidados)