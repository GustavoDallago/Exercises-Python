'''
Você foi contratado(a) como cientista de dados de uma associação de skate.
Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano,
você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso,
o seu código deve receber 5 notas digitadas pelas pessoas juradas.
'''
notas = []
for i in range(5):
 nota = float(input(f'Digite a nota {i+1}: '))
 notas.append(nota)

med_notas = lambda n1,n2,n3,n4,n5: (n1 + n2 + n3 + n4 + n5) / 5
med_final = med_notas(*notas)
med_final