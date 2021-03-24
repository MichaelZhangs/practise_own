import math

def fun(num):
    lst = range(2,num+1)
    ret = [ ]
    for n in lst:
        print("--->", n)
        for k in range(2,int(math.sqrt(n)) + 1):
            print("====>", k)
            if n % k == 0:
                break
        else:
                ret.append(n)
    print(ret)
fun(10)