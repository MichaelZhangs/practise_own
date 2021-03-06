#coding:utf8
import threading
import time

def sayHi():
    print("hi","--->",threading.currentThread().name, threading.current_thread().getName())
    time.sleep(1)

def run():
    lst = [ ]
    for i in range(5):
        t = threading.Thread(target=sayHi)
        lst.append(t)
    for th in  lst:
        th.start()


if __name__ == '__main__':
    run()