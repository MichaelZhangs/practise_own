while True:
    try:
        # split()分割所有空白字符
        n, k = input().split()
        n_list = input()
        x = [int(i) for i in n_list.split()]
        x = sorted(x)
        x = x[:int(k)]
        # 要用map转到str。。
        print(' '.join(map(str, x)))

    except:
        break