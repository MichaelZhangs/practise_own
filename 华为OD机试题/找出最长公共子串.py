def findsub(a,b):

    if len(a) > len(b):
        a,b = b, a

    leng = 0
    for i in range(len(a)):
        for j in range(i,len(a) + 1):
            res = a[i:j]
            if res in b and j - i > leng:
                sub = res
                leng = j - i
    return sub
while True:
    try:
        a = input()
        b = input()
        print(findsub(a,b))
    except:
        break

