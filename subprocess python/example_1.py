"""
    subprocess:
        doc -> https://docs.python.org/3/library/asyncio-subprocess.html
"""

import asyncio


async def main():
    process = await asyncio.create_subprocess_exec('python', 'example_2.py', stdin=asyncio.subprocess.PIPE,
                                                   stdout=asyncio.subprocess.PIPE)
    std_out, std_err = await process.communicate(b'mohammadhssn')
    print(f'std_out: {std_out}')
    print(f'std_err: {std_err}')


asyncio.run(main())
