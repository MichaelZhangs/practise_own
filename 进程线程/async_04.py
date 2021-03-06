#encoding:utf8
import time
import asyncio

async def countdown(number,n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1
#方式一
# start = time.time()
# loop = asyncio.get_event_loop()
# tasks = [
#         asyncio.ensure_future(countdown('A', 2)),
#         asyncio.ensure_future(countdown('B', 3))
#     ]
#
# loop.run_until_complete(asyncio.wait(tasks))

# print(time.time() - start)
# 方式二
def run():
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(countdown('A', 2)),
        asyncio.ensure_future(countdown('B', 3))
    ]
    # tasks = [
    #     loop.create_task(countdown('A', 2)),
    #     loop.create_task(countdown('B', 3))
    # ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
if __name__ == '__main__':
    # run()  #需要对应asyncio.ensure，加入函数
    run()