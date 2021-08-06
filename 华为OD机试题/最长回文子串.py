def huiwen():
    while True:
        try:
            a = input()
            for i in range(len(a),1,-1):
                for j in range(len(a) -i + 1):
                    # print(i, j)
                    res = a[j:i+j]
                    if res == res[::-1]:
                        print(res)
                        return i
        except:
            break
print(huiwen())