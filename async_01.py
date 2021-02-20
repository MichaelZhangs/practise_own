#coding:utf8
from time import sleep, strftime, time
import asyncio
import threading

async def display(*args):
    # await asyncio.sleep(1)
    print(strftime('[%H:%M:%S]'), end=" ")
    print(*args)

async  def loiter(n):
    msg = '{} start --> {}s....'
    await display(msg.format(n, n))
    # sleep(n)
    # await asyncio.sleep(n)
    print("---->", threading.current_thread())
    msg = '{} end '
    await display(msg.format(n))
    return n * 10

async def main():
    tasks = []
    for i in range(5):
        print("========")
        t = asyncio.create_task(loiter(i))  #只能放在函数里面，如果main()函数放到外面，则报错
        tasks.append(t)
    print(tasks)

if __name__ == '__main__':
    start = time()
    asyncio.run(main())
    end = time()
    print("--->", end - start)

# asyncio.run(main())

