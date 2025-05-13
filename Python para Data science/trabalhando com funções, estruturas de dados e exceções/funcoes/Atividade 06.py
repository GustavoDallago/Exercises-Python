'''
Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes,
você precisa criar uma função que receba uma lista de 4 notas e retorne:
'''
def med_estudante():
  notas_estudante = []
  for i in range(4):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas_estudante.append(nota)
  media_notas = lambda nota: sum(nota)/4
  media = media_notas(notas_estudante)
  if media >= 7:
    print(f'O estudante foi aprovado com média {media}, sendo sua maior nota: {max(notas_estudante)} e sua menor nota {min(notas_estudante)}')
  else:
    print(f'O estudante foi reprovado com média {media}, sendo sua maior nota: {max(notas_estudante)} e sua menor nota {min(notas_estudante)}')

med_estudante()