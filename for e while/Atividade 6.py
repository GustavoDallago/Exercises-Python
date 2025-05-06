livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

nome_livro = input('Digite o nome do livro que procura: ')

for nome_livro in livros:
    if nome_livro == 'O Pequeno Príncipe':
      print(f'Livro encontrado {nome_livro}')
      break
    elif nome_livro != 'O Pequeno Príncipe':
      continue
    else:
      print('Livro não encontrado')