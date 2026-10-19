import asyncio

async def task(name, sem):
    async with sem:
        print(name + " начал")
        await asyncio.sleep(1)
        print(name + " закончил")

async def main():
    sem = asyncio.Semaphore(2)  # только 2 одновременно
    await asyncio.gather(
        task("A", sem),
        task("B", sem),
        task("C", sem),
        task("D", sem)
    )

asyncio.run(main())