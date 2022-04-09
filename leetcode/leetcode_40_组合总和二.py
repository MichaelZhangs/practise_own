"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
from typing import List
class Solution:
    def __init__(self):
        self.count = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        # 回溯
        def dfs(path_, target, index):

            if target == 0:
                res.append(path_[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                # if candidates[i] > target:
                #     break
                path_.append(candidates[i])
                self.count += 1
                dfs(path_ , target-candidates[i], i + 1)
                path_.pop()
        dfs([], target, 0)
        print(self.count)
        return res
        #
        # def dfs(tmp, cur, index):
        #     if cur == target:
        #         res.append(tmp)
        #         return
        #     for i in range(index, len(candidates)):
        #         if i > index and candidates[i] == candidates[i - 1]:
        #             continue
        #         if cur > target:
        #             break
        #         self.count += 1
        #         dfs(tmp + [candidates[i]], cur + candidates[i], i + 1)
        # dfs([], 0, 0)
        # print(self.count)
        # return res


        # def dfs(p,  idx):
        #     if sum(p) == target:
        #         res.append(p[:])
        #         return
        #     for i in range(idx, len(candidates)):
        #         if i > idx and candidates[i] == candidates[i - 1]:
        #             continue
        #         if candidates[idx] > target:
        #             break
        #         self.count += 1
        #         p.append(candidates[i])
        #         dfs(p,  i + 1)
        #         p.pop()
        # dfs([],  0)
        # print(self.count)
        # return res
if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5,-1]
    target = 9
    # candidates = [1, -2, -5, -4, -3, 3, 3, 5]
    # target = -11  [[-1, 1, 1, 2, 6], [-1, 1, 2, 7], [-1, 10], [1, 1, 2, 5], [1, 1, 7], [1, 2, 6], [2, 7]]
    print(Solution().combinationSum2(candidates, target))
    """
   
    """