"""
    Cancel
"""

import asyncio


async def one():
    await asyncio.sleep(7)
    print('Hello...')


async def main():
    task_one = asyncio.create_task(one())

    # try:
    #     await asyncio.wait_for(task_one, timeout=5)
    # except asyncio.TimeoutError:
    #     print('task cancel')
    # print(f'task is cancelled? {task_one.cancelled()}')

    try:
        await asyncio.wait_for(asyncio.shield(task_one), timeout=5)
    except asyncio.TimeoutError:
        print('task is taking longer than usual, but we are working on it.')
        await task_one


asyncio.run(main())
