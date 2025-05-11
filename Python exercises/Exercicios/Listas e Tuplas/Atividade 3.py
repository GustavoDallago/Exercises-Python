participantes = []

while True:
    nome = input('Insira o nome do participante (ou digite "sair"): ')
    if nome.lower() == 'sair':
        break
    participantes.append(nome)

print(participantes)