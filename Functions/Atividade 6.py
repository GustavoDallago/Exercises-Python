numeros = input('Digite os números separados por espaço: ').split()
numeros_int = map(int, numeros)

def num_pares(valor):
    return valor % 2 == 0

pares = filter(num_pares, numeros_int)

print(list(pares))