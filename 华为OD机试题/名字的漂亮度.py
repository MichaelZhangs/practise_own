from collections import Counter


def count_name():
    while True:
        try:
            s = int(input())
            for i in range(s):
                s_str = input().strip().lower()
                s_list = sorted(Counter(s_str).values(), reverse=True)
                total = 0
                for i in range(len(s_list)):
                    total += (26 - i) * s_list[i]
                print(total)

        except:
            break


count_name()