def muda_stg_int():
    valores = input('Digite os valores das vendas: ')
    separa_valores = valores.split()
    valores_int = []
    for valor in separa_valores:
        valores_int.append(int(valor))
    soma = sum(valores_int)
    print(f'O total de vendas foi: {soma}')

muda_stg_int()