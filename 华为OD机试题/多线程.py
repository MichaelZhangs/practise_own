from concurrent.futures import ThreadPoolExecutor


def add_s(s):
    res = []
    res.append(s)
    return res


lst = ['A', 'B', 'C', 'D']
while True:
    try:

        n = int(input())
        while n:
            executor = ThreadPoolExecutor(max_workers=4)
            res = executor.map(add_s, lst)
            for i in res:
                print(i[0], end="")
            n -= 1
        print()

    except:
        break