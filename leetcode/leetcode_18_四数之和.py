"""
四数之和
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
"""
from typing import List
def fourSum(nums: List[int], target:int) -> List[List[int]]:
    res = []
    if len(nums) < 4 or not nums:
        return res
    nums.sort()
    if len(nums) < 4: return []
    nums.sort()
    result = []

    for idx in range(len(nums) - 3):
        if nums[idx] + nums[idx + 1] * 3 > target:
            break
            # 这是加速项目，如果当前位置的数字+剩余位置数位的下一个数的倍数>target，
            # 则分析当前位置无意义
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue
            # 如果当前的索引已经不是第一位的了，
            # 就要走到一个跟上一个不一样数字的索引上去
        if nums[idx] + nums[-1] * 3 < target:
            continue  # 这是加速项目，
            # 如果当前位置的数字+剩余位置数位的最后（大）数的倍数<target，则分析当前位置无意义

        for i in range(idx + 1, len(nums) - 2):
            if nums[idx] + nums[i] + nums[i + 1] * 2 > target:
                break
            if nums[idx] + nums[i] + nums[-1] * 2 < target:
                continue
            if i > idx + 1 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[idx] + nums[i] + nums[j] + nums[k]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    result.append([nums[idx], nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    j += 1
                    k -= 1
    return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(fourSum(nums, target))