import asyncio
import aiohttp
import time
from flags import BASE_URL, save_flag, show, main

async def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = await aiohttp.request("GET", url)
    image = await resp.read()
    return  image

async def down_loadone(cc):
    image = await get_flag(cc)
    show(cc)
    save_flag(image, cc.lower()+".gif")
    return cc

async def dowload_many(cc_list):
    tasks = [ down_loadone(cc) for cc in sorted(cc_list)]
    asyncio.run(asyncio.wait(tasks))
    return len(cc_list)

if __name__ == '__main__':
    start = time.time()
    main(dowload_many)
    print("---->",time.time() - start)