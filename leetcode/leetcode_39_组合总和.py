"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，
并以列表形式返回。你可以按 任意顺序 返回这些组合
"""

from typing import List


class Solution:
    def combinationSum(self, candidates:List[int], target: int) ->List[List[int]]:

        # def dfs(candidates, begin, size, path, res, target):
        #
        #     if target == 0:
        #         res.append(path)
        #         return
        #
        #     for index in range(begin, size):
        #         residue = target - candidates[index]
        #         if residue < 0:
        #             break
        #
        #         dfs(candidates, index, size, path + [candidates[index]], res, residue)
        #
        # size = len(candidates)
        # if size == 0:
        #     return []
        # candidates.sort()
        # path = []
        # res = []
        # dfs(candidates, 0, size, path, res, target)
        # return res
        res = []

        def dfs(path, target, candidate):
            if target == 0:
                res.append(path)
                # print(res)
            for i in range(len(candidate)):
                if target >= candidate[i]:
                    dfs(path+[candidate[i]], target-candidate[i], candidate[i:])
        dfs([], target, candidates)
        return res


if __name__ == '__main__':
    candidates = [4,2, 3, 6, 7]
    target = 7

    r = Solution().combinationSum(candidates, target)
    print(r)