'''
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as
para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: nome.capitalize() + " "+ sobrenome.capitalize(), nomes,sobrenomes)
nome_finalizado = list(nome_completo)
nome_finalizado

for dados in nome_finalizado:
  print(dados)