import asyncio
import aiohttp

async def get_weather(session, city, sem):
    async with sem:
        async with session.get("https://wttr.in/" + city + "?format=3") as r:
            text = await r.text()
            print(text.strip())

async def main():
    cities = ["Лянтор", "Moscow", "Piter", "Kazan", "Omsk"]
    sem = asyncio.Semaphore(3)

    async with aiohttp.ClientSession() as session:
        tasks = [get_weather(session, c, sem) for c in cities]
        await asyncio.gather(*tasks)

asyncio.run(main())