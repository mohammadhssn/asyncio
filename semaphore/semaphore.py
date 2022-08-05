"""
    semaphore:
        doc -> https://docs.python.org/3/library/asyncio-sync.html#semaphore
        BoundedSemaphore -> https://docs.python.org/3/library/asyncio-sync.html#boundedsemaphore
"""

import asyncio


async def show(smp):
    async with smp:
        print('show is working ...')
        await asyncio.sleep(1)


async def main():
    smp = asyncio.Semaphore(value=2)
    # smp = asyncio.BoundedSemaphore(value=2)
    await asyncio.gather(*[show(smp) for _ in range(10)])


asyncio.run(main())
