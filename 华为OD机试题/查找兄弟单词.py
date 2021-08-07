while True:
    try:
        s_list = input().split()
        num, k = int(s_list[0]), int(s_list[-1])
        words = s_list[1: 1 + num]
        find_word = s_list[-2]
        res = []
        for i in words:
            if sorted(i) == sorted(find_word) and i != find_word:
                res.append(i)
        print(len(res))
        print(sorted(res)[k-1])
    except:
        break