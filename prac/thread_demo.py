from concurrent.futures import ThreadPoolExecutor
import threading
import json
from queue import Queue
lst = [ json.dumps({str(i):str(i * 2)}) for i in range(100)]
print(type(lst[0]))

executor = ThreadPoolExecutor(max_workers=5)
res = executor.map(json.loads, lst)
for i in res:
    print(i)
    # print(type(i))
q = Queue(20)

def readS():
    for s in lst:
        q.put(s)

def getS():
    print("---->", threading.current_thread())
    while True:
        if q.empty():
            break
        s = q.get()
        print(json.loads(s))

for k in range(1):
    k = threading.Thread(target=readS,)
    k.start()
for i in range(5):
    t = threading.Thread(target=getS,)
    t.start()


