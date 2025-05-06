#Crie um programa que receba o número de vendas dos dois produtos e exiba 
#uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, 
#exiba uma mensagem dizendo que houve empate.

macas = int(input('Digite a quantidade de maças vendidas: '))
banana = int(input('Digite a quantidade de bananas vendidas no mês: '))

if  banana < 0 or macas <0:
    print('Quantidade inserida é inválida')
else:
  if macas > banana:
      print('Mais maças foram vendidas')
  elif banana > macas:
      print('Mais bananas foram vendidas')