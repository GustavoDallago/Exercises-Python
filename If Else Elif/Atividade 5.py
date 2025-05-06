#Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
#Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um 
#programa que ajude a controlar suas despesas. O programa deve receber o total 
#de despesas realizadas e informar se ele ultrapassou o limite ou ainda está 
#dentro do orçamento.

despesa = float(input('Insira o total de despesas do mês: '))

if despesa >= 3000:
  print(f'As suas desesas R${despesa} estão acima do limite estabelecido')
else:
  print(f'As suas desesas R${despesa} estão dentro do limite estabelecido')