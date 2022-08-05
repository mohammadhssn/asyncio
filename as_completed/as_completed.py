"""
    as_completed():
        doc -> https://docs.python.org/3/library/asyncio-task.html?highlight=as_completed#asyncio.as_completed
"""

import aiohttp
import asyncio


async def show_status(session, url, delay):
    async with session.get(url) as response:
        await asyncio.sleep(delay)
        print(f'status for {url} is {response.status}')


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, 'https://www.wikipedia.org/', 5),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_language', 2),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_Gulf', 4),
            show_status(session, 'https://en.wikipedia.org/wiki/Persian_cat', 7),
        ]

        for request in asyncio.as_completed(requests):  # convert to future
            await request


asyncio.run(main())
