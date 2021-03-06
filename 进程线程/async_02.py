#encoding:utf8
import aiohttp
import asyncio
import requests
import time
async def test1(i):
    r = await test2(i)
    print(i,"--->", r)
    return 10

async def test2(i):

    r = requests.get( i)
    print(i)
    await asyncio.sleep(1)
    
    return r

async def main():
    url = ["https://www.baidu.com/","https://www.sohu.com/"]
    # loop = asyncio.get_event_loop()
    tasks = [ asyncio.create_task(test1(i)) for i in url]
    print(tasks)
    # loop.run_until_complete(asyncio.wait(tasks))
# asyncio.run(asyncio.wait(tasks))
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print("--->", time.time() - start)
