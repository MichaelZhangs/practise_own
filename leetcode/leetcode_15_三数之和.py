"""
三数之和
"""
from typing import List
def threeSum(nums: List[int], target: int) -> List[List[int]]:
    ans = []
    if len(nums) < 3:
        return ans
    nums.sort()
    for i in range(len(nums) - 2):
        # 如果最小的三个数已经大于 0，退出程序
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break
        # 如果最大的三个数还小于0，continue
        if nums[i] + nums[-1] + nums[-2] < 0:
            continue
        # 如果当前这个数等于前一个数， continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 双指针
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            # 如果三数之和等于 0，
            if three_sum == 0:
                ans.append([nums[i], nums[left], nums[right]])
                # 去除重复的左边元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # 去除重复的右边元素
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # 更新 left， right的值
                left += 1
                right -= 1
            # 如果三数之和小于 0
            elif three_sum < 0:
                left += 1
            # 如果三数之和大于 0
            else:
                right -= 1
    return ans

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums, 0))
