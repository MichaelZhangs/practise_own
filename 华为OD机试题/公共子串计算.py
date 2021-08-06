while True:
    try:
        s = input()
        m = input()
        if len(s) > len(m):
            s,m = m,s
        i = 0
        max_leng = 0
        while i + max_leng < len(s):
            while s[i:i + max_leng + 1] in m and  i + max_leng < len(s):
                max_leng += 1
            i += 1
        print(max_leng)
    except:
        break