from typing import List
"""
存在超时
"""
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        leng = len(nums)
        res = []
        target = target
        visited = [False] * leng
        def dfs(path_, nums_list, idx):
            if len(path_) > 4:
                return
            if len(path_) == 4 and sum(path_) == target:
                res.append(path_[:])
            s = set()
            for i in range(idx, leng):
                if visited[i] or nums_list[i] in s:
                    continue
                if i > idx and nums_list[i] == nums_list[i - 1]:
                    continue

                path_.append(nums_list[i])
                visited[i] = True
                s.add(nums_list[i])
                dfs(path_, nums_list, i + 1)
                visited[i] = False
                path_.pop()
        nums.sort()
        dfs([], nums, 0)



        return res
if __name__ == '__main__':
    # nums = [-1,0,1,2,-1,-4]
    # target = -1
    # nums = [7,1,7,-7,10,3,-5,-3,-9,6,-8,-6,-10,10,-3,4,2]
    # target = 18
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    target = -11
    print(Solution().threeSum(nums, target))



if __name__ == '__main__':
    pass
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        
        def Search(i, target, oneSolution, notSelected):
            if target == 0 and len(oneSolution) == 4:
                output.append(oneSolution)
                return
            elif len(oneSolution) > 4 or i >= len(nums):
                return

            if target - nums[i] - (3 - len(oneSolution)) * nums[-1] > 0 or nums[i] in notSelected:
                Search(i + 1, target, oneSolution, notSelected)
            elif target - (4 - len(oneSolution)) * nums[i] < 0:
                return
            else:
                Search(i + 1, target, oneSolution, notSelected + [nums[i]])
                Search(i + 1, target - nums[i], oneSolution + [nums[i]], notSelected)


        Search(0, target, [], [])

        return output

"""