texto1 = set(input("Texto 1: ").lower().split())

texto2 = set(input("Texto 2: ").lower().split())    

comum = texto1.intersection(texto2)

print(comum)