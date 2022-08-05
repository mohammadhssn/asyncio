"""
    lock:
        doc -> https://docs.python.org/3/library/asyncio-sync.html#lock
"""

import asyncio

counter = 0


async def increment(lock):
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.01)
        counter = temp_counter


async def main():
    lock = asyncio.Lock()

    tasks = [increment(lock) for _ in range(100)]
    await asyncio.gather(*tasks)

    print(f'counter is {counter}')  # without lock counter is 1 || with lock counter is 100


asyncio.run(main())
