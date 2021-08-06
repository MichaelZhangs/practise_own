while True:
    try:
        a = input()
        while(len(a) >= 8):
            print(a[:8])
            a = a[8:]
        if len(a) > 0:
            print(a + '0'*(8 - len(a)))
    except:
        break