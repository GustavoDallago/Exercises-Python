'''
Você recebeu o desafio de criar um código que calcula os gastos de uma viagem
para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na
viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro.
O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente
[850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos
com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
'''

#150 a diária
#14 km/l - R$5 por litro

cidades = ['Salvador', 'Fortaleza', 'Natal', 'Aracaju']
gastos_passeio = [200, 400, 250, 300]
distancia_cidades = [850, 800, 300, 550]

destino_viagem = int(input(f'escolha entre as quatro cidades (digite entre 1 a 4 para as respctivas cidades) {cidades}: '))
dias_viagem = int(input('Quantos dias de viagem? '))

def gastos_hoteis():
  gasto_hotel = 150 * dias_viagem
  return gasto_hotel

def gastos_gasolina():
  gastos_gasolina = int((distancia_cidades[destino_viagem - 1] / 14) *5) *2
  return gastos_gasolina

def gastos_alimentacao():
  gastos_alimentacao = gastos_passeio[destino_viagem - 1] * dias_viagem
  return gastos_alimentacao

print(f'Gasto com hotel: R${gastos_hoteis()}')
print(f'Gasto com gasolina: R${gastos_gasolina()}')
print(f'Gasto com passeio e alimentação: {gastos_alimentacao()}')