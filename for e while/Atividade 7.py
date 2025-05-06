itens_estoque = int(input('Digite a quantidade de itens no estoque: '))

while itens_estoque >= 0:
  if itens_estoque > 0:
    print(f'Venda realizada! Estoque restante: {itens_estoque}')
    itens_estoque = itens_estoque - 1
  elif itens_estoque == 0:
    print('Estoque esgotado')
    break