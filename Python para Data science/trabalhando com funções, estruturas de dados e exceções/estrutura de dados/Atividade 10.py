funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
agrupado = {}

for estado, qtd in funcionarios:
    if estado in agrupado:
        agrupado[estado].append(qtd)
    else:
        agrupado[estado] = [qtd]
        
somas = {
    estado: sum(agrupado[estado])
    for estado in agrupado
}

print(somas)