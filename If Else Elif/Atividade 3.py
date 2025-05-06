#Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de
#servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura 
#atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura = int(input('Insira a atual temperatura dos servidores: '))

if temperatura > 25:
  print('ALERTA! temperatura acima do limite permitido')
elif temperatura < 25:
  print('Temperatura dentro do limite permitido')
else:
  print('Temperatura igual ao limite permitido')