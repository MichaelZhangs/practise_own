"""
给定一个不含重复数字的数组 nums ，
返回其 所有可能的全排列 。
你可以 按任意顺序 返回答案。

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        leng = len(nums)
        visited = [False] * leng
        def dfs(path_):
            if len(path_) == leng:
                res.append(path_[:])
            s = set()
            for i in range(leng):
                if nums[i] in s or  visited[i]:
                    continue
                visited[i] = True
                
                path_.append(nums[i])
                s.add(nums[i])
                dfs(path_)
                visited[i] = False
                path_.pop()
        dfs([])
        return res


if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().permute(nums))
