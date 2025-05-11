#Escreva um programa que receba três notas como entrada e calcule a média final.
#Com base na média, exiba a situação do aluno.

nota1 = float(input('Insira a nota 1: '))
nota2 = float(input('Insira a nota 2: '))
nota3 = float(input('Insira a nota 3: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
  print(f'Aprovado {media:.2f}')
elif 5 <= media < 7:
  print(f'Recuperação {media:.2f}')
else:
  print(f'Reprovado {media:.2f}')