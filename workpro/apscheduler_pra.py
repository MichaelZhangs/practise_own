from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor

class A:

    def printA(self):
        print("aaaaa")
a = A()

#多进程执行

executors = {
    "default": ProcessPoolExecutor(3)
}

schedu = BlockingScheduler(executors=executors)

schedu.add_job(a.printA, trigger="interval", seconds=5)


if __name__ == '__main__':
    schedu.start()