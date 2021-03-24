ret = [ ]
lst = [ ]
num = 12
def findNum():
    for i in range(2, num+1):
        if num % i == 0:
            ret.append(i)
            break
def judge(num):

        if num % ret[0] == 0:
            lst.append(ret[0])
            num /= ret[0]

            return judge(num)
def fun():
    s = 1
    for i in lst:
        s *= i
    if s == num:
        return  True
    return  False

findNum()
judge(num)
print(fun())



