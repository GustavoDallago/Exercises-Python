#Crie um programa que receba como entrada a renda mensal de Pedro e o valor da 
#parcela desejada. O programa deve informar se o empréstimo foi aprovado ou 
#negado com base nas condições acima.

renda = float(input('Insira a sua renda mensal: '))
parcela = float(input('Insira o valor da parcela desejada: '))
verificador_parcela = renda * 0.3

if parcela <= verificador_parcela:
  print(f'Emprestimo de R${parcela} aprovado')
else:
   print(f'Emprestimo de R${parcela} negado')