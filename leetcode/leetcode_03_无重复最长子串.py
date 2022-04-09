"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


def fun(s: str) -> int:
    ret = []
    big = 0
    for i in range(0,len(s)):
        for j in range(i+1, len(s)+1):
            res = s[i:j]
            if len(res) == len(set(res)):
                # if len(res) > big:
                #     big = len(res)
                #     print(res)
                big = max(big, len(res))
    return big
def fun2(s):
    if len(s) <= 1:
        return len(s)
    char_map, left, ans = dict(), -1, 0
    for i, char in enumerate(s):
        if char not in char_map:
            char_map[char] = i
        else:
            left = max(left, char_map[char])
            char_map[char] = i
        ans = max(ans, i - left)

    return ans

if __name__ == '__main__':
    s = "a"
    print(fun(s))