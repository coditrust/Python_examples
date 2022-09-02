import asyncio

async def nested():
    return 42

async def main():
    # Attendons le résultat de nested()
    print(await nested()) # affichera "42"

asyncio.run(main())
