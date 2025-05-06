#Escreva um programa que receba o número de dias de três atividades e exiba o
#tempo total do projeto. Se algum valor for negativo, mostre uma mensagem 
#informando o erro.

atividadeA = int(input('Insira a quantidade de dias para entregar a atividade A: '))
atividadeB = int(input('Insira a quantidade de dias para entregar a atividade B: '))
atividadeC = int(input('Insira a quantidade de dias para entregar a atividade C: '))

if atividadeA < 0 or atividadeB <0 or atividadeC <0:
  print('Erro: Os dias não podem ser negativos')
else:
  print(f'O tempo de conclusão do projeto é de {atividadeA + atividadeB + atividadeC} dias')