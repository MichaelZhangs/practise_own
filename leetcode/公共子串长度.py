"""
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
asdfas
werasdfaswer
6
"""


def zichuan(a: str, b: str) -> int:
    if len(a) > len(b):
        a, b = b, a
    Max = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i:j + 1] in b and j + 1 - i > Max:
                Max = j + 1 - i
    return Max


if __name__ == '__main__':
    while True:
        try:
            a = input()
            b = input()
            n = zichuan(a, b)
            print(n)
        except:
            break
