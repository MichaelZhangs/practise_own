#coding:utf8
from time import sleep, strftime, time
import asyncio
import threading

async def display(*args):
    # await asyncio.sleep(1)
    print("又来了。。。。")
    print(strftime('[%H:%M:%S]'), end=" ")
    print(*args)

async  def loiter(n):
    msg = '{} start --> {}s....'
    await display(msg.format(n, n))
    # sleep(n)
    await asyncio.sleep(n)
    print("---->", threading.current_thread())
    msg = '{} end '
    await display(msg.format(n))
    print("hahah")
    return n * 10

# async def main():
#     tasks = []
#     for i in range(5):
#         t = asyncio.create_task(loiter(i))  #只能放在函数里面，如果main()函数放到外面，则报错
#         tasks.append(t)
#     print(tasks)
#能完全运行结果,即使休眠
def main():
    tasks = []
    loop = asyncio.get_event_loop()
    for i in range(5):
        t = loop.create_task(loiter(i))
        tasks.append(t)
    t,k  = loop.run_until_complete(asyncio.wait(tasks))
    print(t)
    print(k)
    print(tasks)
if __name__ == '__main__':
    start = time()
    # asyncio.run(main())
    main()
    end = time()
    print("--->", end - start)

# asyncio.run(main())

