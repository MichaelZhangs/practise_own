"""
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案

s = "wordgoodgoodgoodbestword",
words = ["word","good","best","word"]

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
"""



from collections import Counter
from typing import List


def findSubstr(s: str, words:List[str]) -> List[int]:
    word = Counter(words)
    print(word)
    m = len(words)
    n = len(words[0])
    all_len = m * n
    s_len = len(s)
    idx = []
    for i in range(0, s_len - all_len + 1):
        temp = []
        for j in range(i, all_len + i, n):
            temp.append(s[j:j + n])
        if word == Counter(temp):
            idx.append(i)
    return idx

if __name__ == '__main__':
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(findSubstr(s, words))