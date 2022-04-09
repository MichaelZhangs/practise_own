"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组
（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""
from typing import List
def f( nums: List[int]) -> int:
    # size = len(nums)
    # pre = 0
    # res = nums[0]
    # t = []
    # for i in range(size):
    #     pre = max(nums[i], pre + nums[i])
    #     res = max(res, pre)
    # return res
    size = len(nums)
    if size == 0:
        return 0
    dp = [0 for _ in range(size)]

    dp[0] = nums[0]
    for i in range(1, size):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]
    print(dp)
    return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        print(nums)
        return max(nums)
if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f(nums))
    print(Solution().maxSubArray(nums))