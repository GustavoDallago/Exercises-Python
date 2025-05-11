atletas = ['Ana', 'João', 'Pedro']

print(atletas)
nome_errado = input('Insira o nome que deseja alterar: ')

if nome_errado in atletas:
    nome_corrigido = input('\nInsira o novo atleta ou o nome corrigido: ')
    posicao = atletas.index(nome_errado)
    atletas.remove(nome_errado)
    atletas.insert(posicao, nome_corrigido)
    print(f"O nome {nome_errado} foi substituído por {nome_corrigido}.")
    print("Lista atualizada:", atletas)