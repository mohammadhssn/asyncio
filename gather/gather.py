"""
    gather:
        doc -> https://docs.python.org/3/library/asyncio-task.html?highlight=gather#asyncio.gather
"""

import aiohttp
import asyncio


async def show_status(session, url):
    async with session.get(url) as response:
        return response.status


async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            'https://www.wikipedia.orgwrongggggggggggggggggggggggggg/',
            'https://en.wikipedia.org/wiki/Persian_language',
            'https://en.wikipedia.org/wiki/Persian_Gulf',
            'https://en.wikipedia.org/wiki/Persian_cat',
        ]

        requests = [show_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests, return_exceptions=True)
        print(status_code)


asyncio.run(main())
