"""
    wait:
        doc -> https://docs.python.org/3/library/asyncio-task.html?highlight=as_completed#waiting-primitives
"""

import aiohttp
import asyncio


async def show_status(session, url, delay=1):
    async with session.get(url) as response:
        await asyncio.sleep(delay)
        return f'status for {url} is {response.status}'


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, 'https://www.wikipedia.org/', 8)),
            asyncio.create_task(show_status(session, 'https://en.wikipedia.org/wiki/Persian_language')),
        ]
        done, pending = await asyncio.wait(requests, timeout=5)  # return_when => asyncio.ALL_COMPLETED
        print(f'done->> {done}')
        print(f'pending->> {pending}')

        for d in done:
            if d.exception() is None:
                print(d.result())
                # print(await d)
            else:
                print('error...')

        for p in pending:
            p.cancel()

        print(f'pending after cancel -> {pending}')


# ---------------------------------------------------------------------------------------------------------------------

async def main_2():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, 'https://www.wikipedia3333333333333333333333.org/')),
            asyncio.create_task(show_status(session, 'https://en.wikipedia.org/wiki/Persian_language')),
        ]
        done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_EXCEPTION)
        print(f'done->> {done}')
        print(f'pending->> {pending}')

        for d in done:
            if d.exception() is None:
                print(d.result())
                # print(await d)
            else:
                print('error...')

        for p in pending:
            p.cancel()

        print(f'pending after cancel -> {pending}')


# ---------------------------------------------------------------------------------------------------------------------
async def main_3():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, 'https://www.wikipedia.org/')),
            asyncio.create_task(show_status(session, 'https://en.wikipedia.org/wiki/Persian_language')),
        ]
        done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_COMPLETED)
        print(f'done->> {done}')
        print(f'pending->> {pending}')

        for d in done:
            if d.exception() is None:
                print(d.result())
                # print(await d)
            else:
                print('error...')

        for p in pending:
            p.cancel()

        print(f'pending after cancel -> {pending}')


asyncio.run(main())
print('=' * 200)
asyncio.run(main_2())
print('=' * 200)
asyncio.run(main_3())
