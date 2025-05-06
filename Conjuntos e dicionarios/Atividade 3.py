listaLaura = set(input("Lista Ana: ").lower().split())   
ListaAna = set(input("Lista Laura: ").lower().split())   

emComum = listaLaura.intersection(ListaAna)
difLaura = listaLaura.difference(ListaAna)
difAna = ListaAna.difference(listaLaura)

print(f'\nItens em comum: {emComum}')
print(f'Itens diferentes da Laura: {difLaura}')
print(f'Itens diferentes da Ana: {difAna}')