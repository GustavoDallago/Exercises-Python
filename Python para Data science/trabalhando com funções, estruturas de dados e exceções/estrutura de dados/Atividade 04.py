aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

alugueis = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']

print(alugueis)