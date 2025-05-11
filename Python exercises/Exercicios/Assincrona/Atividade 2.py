import asyncio

async def informacao(numero):
  print(f'Iniciando {numero}')
  await asyncio.sleep(3)
  print(f'{numero} finalizado')

async def main():
  tarefa1 = asyncio.create_task(informacao("Download"))
  tarefa2 = asyncio.create_task(informacao("Analise de dados"))
  await tarefa1
  await tarefa2

asyncio.run(main())