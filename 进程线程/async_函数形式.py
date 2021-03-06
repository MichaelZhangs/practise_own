import time
import asyncio

# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.

async def countdown(number,n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1

def run():
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(countdown('A', 2)),
        loop.create_task(countdown('B', 3))
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    start = time.time()
    run()
    print("--->", time.time() - start)