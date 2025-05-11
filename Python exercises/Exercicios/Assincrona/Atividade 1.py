import asyncio

async def corrotina():
  print('Iniciando validação')
  await asyncio.sleep(3)
  print('Validação finalizada')

asyncio.run((corrotina()))