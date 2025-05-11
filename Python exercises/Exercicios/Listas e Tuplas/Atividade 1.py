despensa = ['Arroz', 'Feijão', 'carne']
comida = input('Digite um alimento: ')

if comida != despensa:
    print(f'O item {comida} precisa ser comprado')
elif comida == despensa:
    print('Item na despensa')  