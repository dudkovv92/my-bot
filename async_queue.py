import asyncio

async def producer(queue):
    for i in range(1, 6):
        print("Положил:", i)
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print("Взял:", item)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(main())