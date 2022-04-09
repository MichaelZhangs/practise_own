"""
给你一个字符串 s，请你将 s 分割成一些子串，
使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
"""

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        #判断是否是回文串
        def pending_s(s):
            if s == s[::-1]:
                return True
            return False
            # l, r = 0, len(s) - 1
            # while l < r:
            #     if s[l] != s[r]:
            #         return False
            #     l += 1
            #     r -= 1
            # return True
        #回溯函数，这里的index作为遍历到的索引位置，也作为终止判断的条件
        def back_track(s, index):
            #如果对整个字符串遍历完成，并且走到了这一步，则直接加入result
            if index == len(s):
                result.append(path[:])
                return
            #遍历每个子串
            for i in range(index, len(s)):
                #剪枝，因为要求每个元素都是回文串，那么我们只对回文串进行递归，不是回文串的部分直接不care它
                #当前子串是回文串
                if pending_s(s[index : i + 1]):
                    #加入当前子串到path
                    path.append(s[index: i + 1])
                    #从当前i+1处重复递归
                    back_track(s, i + 1)
                    #回溯
                    path.pop()
        back_track(s, 0)
        return result

if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))