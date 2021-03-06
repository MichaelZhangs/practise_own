from time import strftime
import asyncio

async def show(i):
    print("{} show({})---> start".format(i,i),strftime("%H:%M:%S"))
    await asyncio.sleep(i)
    print("{} show({})---> end".format(i, i), strftime("%H:%M:%S"))

async def func():
    tasks = [ ]
    for i in range(5):
        t = asyncio.create_task(show(i))
        tasks.append(t)
    await asyncio.wait(tasks)
    return i * 10
if __name__ == '__main__':
    # asyncio.run(func())
    loop = asyncio.get_event_loop()
    resp= loop.run_until_complete(func())
    print(resp)
