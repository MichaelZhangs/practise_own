def fun(num):
    if num < 2:
        return True
    a = 2
    b =  num // 2
    while a  <= b:
        x = a + (b - a) // 2
        c = x * x
        print("-->", c)
        if c == num:
            return True
        if c > num:
            b = x - 1
        else:
            a = x + 1

    return  False
a = fun(21)
print(a)
