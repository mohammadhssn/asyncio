"""
    Coroutine
"""

import asyncio
from time import perf_counter

start = perf_counter()


async def one(name):
    await asyncio.sleep(2)
    print(f'hello {name}')


async def main():
    one_1 = asyncio.create_task(one('mohammadhssn'))
    one_2 = asyncio.create_task(one('sara'))

    await one_1
    await one_2


asyncio.run(main())

end = perf_counter()

print(round(end - start))  # 2
