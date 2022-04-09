
from typing import List
"""
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        #  回溯算法
        phone = {'2' :['a' ,'b' ,'c'],
                 '3' :['d' ,'e' ,'f'],
                 '4' :['g' ,'h' ,'i'],
                 '5' :['j' ,'k' ,'l'],
                 '6' :['m' ,'n' ,'o'],
                 '7' :['p' ,'q' ,'r' ,'s'],
                 '8' :['t' ,'u' ,'v'],
                 '9' :['w' ,'x' ,'y' ,'z']}

        def backtrack(conbination ,nextdigit):
            if len(nextdigit) == 0:
                # print("res = ", res)
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    print(conbination, letter, nextdigit)
                    backtrack(conbination + letter ,nextdigit[1:])

        res = []
        backtrack('' ,digits)
        return res
"""
方法 二
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            ans = [pre+suf for pre in ans for suf in KEY[num]]
        return ans
"""

if __name__ == '__main__':
    digits = "234"
    print(Solution().letterCombinations(digits))