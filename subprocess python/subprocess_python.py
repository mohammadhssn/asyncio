"""
    subprocess:
        doc -> https://docs.python.org/3/library/asyncio-subprocess.html
"""

import asyncio


async def main():
    process = await asyncio.create_subprocess_exec('sleep', '5')

    print(f'Process ID is {process.pid}')

    try:
        status_code = await asyncio.wait_for(process.wait(), 2)
        print(f'Status code is {status_code}')
    except asyncio.TimeoutError:
        print('Time out...')
        process.terminate()
        status_code = await process.wait()
        print(f'Status code is {status_code}')


asyncio.run(main())
