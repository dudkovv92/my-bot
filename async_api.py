import asyncio
import aiohttp

async def get(session, url):
    async with session.get(url) as r:
        return await r.text()
async def main():
    urls = [
        "https://wttr.in/Lyantor?format=3",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [get(session, u) for u in urls]
        results = await asyncio.gather(*tasks)
        for r in results:
            print(r)

asyncio.run(main())