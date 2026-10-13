import asyncio
import time
async def task(name, sec):
    print(name + " начал")
    await asyncio.sleep(sec)
    print(name + " закончил")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())

async def hello():
    print("Начало")
    await asyncio.sleep(2)
    print("Прошло 2 секунды")

asyncio.run(hello())