#encoding:utf8
from time import sleep, strftime,time
from concurrent import futures
import threading
def display(*args):
    print(strftime('[%H:%M:%S]'),"---->", threading.current_thread())
    print(*args)

def loiter(n):
    msg = '{} start --> {}s....'
    display(msg.format(n,n))
    sleep(n)
    # print("---->", threading.current_thread())
    msg ='{} end '
    display(msg.format(n))
    # return n * 10

if __name__ == '__main__':
    start = time()
    executor = futures.ThreadPoolExecutor(max_workers = 3)
    executor.map(loiter, range(5))
    # for i in range(5):
    #     loiter(i)
    end = time()
    print("--->",end - start)
    # 5s  启用线程
    #10s 不启用线程


