lista_convidados = ['Ana', 'Pedro', 'Carlos']
novo_convidado = input('Insira um novo convidado: ')
print(lista_convidados)
lugar_convidado = int(input('Insira o numero de chegada desse convidado: '))
posicao = lugar_convidado - 1
lista_convidados.insert(posicao, novo_convidado)
print(lista_convidados)