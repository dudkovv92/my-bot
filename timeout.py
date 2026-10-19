import asyncio

async def slow_task():
    print("Начал")
    await asyncio.sleep(5)
    print("Закончил")
    return "Готово"

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print("Результат:", result)
    except asyncio.TimeoutError:
        print("Не успел за 2 секунды!")

asyncio.run(main())