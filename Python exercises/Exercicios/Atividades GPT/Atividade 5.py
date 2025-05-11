import asyncio

async def download():
    print("Iniciando download...")
    await asyncio.sleep(3)  # Espera 3 segundos
    print("Download concluído!")

async def analise():
    print("Iniciando análise de dados...")
    await asyncio.sleep(2)  # Espera 2 segundos
    print("Análise concluída!")

async def main():
    await asyncio.gather(
        download(),
        analise()
    )

asyncio.run(main())