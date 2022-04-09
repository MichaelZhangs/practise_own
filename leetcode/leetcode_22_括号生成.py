from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curStr = ""
        res = []
        # def dfs(curStr,left, right, n):
        #     if left == n and right == n:
        #         res.append(curStr)
        #         return
        #     # if left < right:
        #     #     return
        #     if left < n:
        #         dfs(curStr + "(", left + 1, right, n)
        #     if right < left:
        #         dfs(curStr + ")", left , right + 1, n)
        # dfs(curStr, 0, 0, n)
        # return res

        # def dfs(p, left, right):
        #     if left > n or right > left:
        #         return
        #     if len(p) == n * 2:
        #         res.append(p)
        #         return
        #     dfs(p + "(", left + 1, right)
        #     dfs(p + ")",left, right + 1 )
        # dfs("", 0, 0)
        #  回溯
        # def backtrace(p, left, right):
        #     print(p)
        #     if left == n and right == n:
        #         res.append("".join(p))
        #         return
        #     if left < n:
        #         p.append("(")
        #         backtrace(p, left + 1, right)
        #         p.pop()
        #     if left > right:
        #         p.append(")")
        #         backtrace(p, left, right + 1)
        #         p.pop()
        # backtrace([], 0, 0)

        def dfs(s, left, right):
            if left == n and right == n:
                res.append(s)
            if left < right:
                return
            if left < n:
                dfs(s + "(", left + 1, right)
            if left > right:
                dfs(s + ")", left, right + 1)

        dfs(curStr, 0, 0)
        return res
if __name__ == '__main__':
    n = 2
    print(Solution().generateParenthesis(n))
