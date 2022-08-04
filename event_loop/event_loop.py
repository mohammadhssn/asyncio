"""
    event loop
"""

import asyncio


async def one(name):
    await asyncio.sleep(3)
    print(f'hello {name}')


async def main():
    task_one_1 = asyncio.create_task(one('mohammadhssn'))
    task_one_2 = asyncio.create_task(one('sara'))

    await task_one_1
    await task_one_2


loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
