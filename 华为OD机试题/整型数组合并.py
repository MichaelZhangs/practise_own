while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))
        m = int(input())
        s2 = list(map(int, input().split()))
        print("".join(map(str, sorted(list(set(s + s2))))))
    except:
        break