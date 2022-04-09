"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        if ls < 3:
            return 0
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(ls):
            L = i + 1
            R = ls - 1
            while L < R :
                total = nums[i] + nums[L] + nums[R]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    R = R - 1
                elif total < target:
                    L = L + 1
                else:
                    return ans
        return ans

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))