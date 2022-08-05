"""
    event:
        doc -> https://docs.python.org/3/library/asyncio-sync.html#event
"""

import asyncio
import functools


def set_trigger(event):
    event.set()


async def do_work_on_even(event):
    print('waiting for event ...')
    await event.wait()
    print('performing work!')
    await asyncio.sleep(2)
    print('finishing work.')
    event.clear()


async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(5, functools.partial(set_trigger, event))
    await asyncio.gather(
        do_work_on_even(event), do_work_on_even(event)
    )


asyncio.run(main())
