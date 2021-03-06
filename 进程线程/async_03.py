import time
import asyncio

async def countdown(number,n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1
# start = time.time()
# loop = asyncio.get_event_loop()
# tasks = [
#         asyncio.ensure_future(countdown('A', 2)),
#         asyncio.ensure_future(countdown('B', 3))
#     ]
#
# loop.run_until_complete(asyncio.wait(tasks))
# print(time.time() - start)
# async  def run():
#     loop = asyncio.get_event_loop()
#     tasks = [
#         asyncio.create_task(countdown('A', 2)),
#         asyncio.create_task(countdown('B', 3))
#     ]
#     loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    #tasks形式1 用asyncio.ensure_future来
    tasks = [
        asyncio.ensure_future(countdown('A', 2)),
        asyncio.ensure_future(countdown('B', 3))
    ]
    #task 形式二 loop.create_task 于 asyncip.ensure_future 等价
    # tasks = [
    #     loop.create_task(countdown('A', 2)),
    #     loop.create_task(countdown('B', 3))
    # ]
    loop.run_until_complete(asyncio.wait(tasks))
    # loop.run_until_complete(asyncio.gather(*tasks))
      #run方法里面传入函数
    print(time.time() - start)