lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
lista_num = []

for i in range(len(lista_de_tuplas)):
    lista_num.append(lista_de_tuplas[i][2])
    
print(lista_num)