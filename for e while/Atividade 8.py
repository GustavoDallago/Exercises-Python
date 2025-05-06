contagem_regressiva = int(10)

while contagem_regressiva >= 0:
  if contagem_regressiva > 0:
    if contagem_regressiva % 2 == 0:
      print(f'Faltam apenas {contagem_regressiva} segundos - Não perca essa oportunidade!')
      contagem_regressiva = contagem_regressiva - 1
    elif contagem_regressiva % 2 != 0:
      print(f'A contagem continua: {contagem_regressiva} segundos restantes.')
      contagem_regressiva = contagem_regressiva - 1
  elif contagem_regressiva == 0:
    print('Aproveite a promoção agora!')
    break