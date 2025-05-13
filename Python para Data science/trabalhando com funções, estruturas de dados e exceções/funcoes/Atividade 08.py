'''
Como cientista de dados em um time de futebol, você precisa implementar novas formas de
coleta de dados sobre o desempenho de jogadores e do time como um todo.
Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato
nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas
de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato.
A função deve retornar a pontuação do time e o aproveitamento em percentual,
levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
'''

gols_marcados = [2, 1, 4, 3, 1]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos():
  pontos_jogos = []
  for i in range(len(gols_marcados)):
    if gols_sofridos[i] > gols_marcados[i]:
      pontos_jogos.append(0)
    elif gols_sofridos[i] < gols_marcados[i]:
      pontos_jogos.append(3)
    else:
      pontos_jogos.append(1)
  total_pontos = sum(pontos_jogos)
  aproveitamento = (total_pontos / (len(gols_marcados) * 3)) * 100

  print(f'Aproveitamento: {aproveitamento}%')

calcula_pontos()