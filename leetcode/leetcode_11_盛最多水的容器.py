"""
盛最多水的容器
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int :
        leng = len(height)
        i = 0
        j = leng - 1
        MaxNum = 0
        ans = 0
        while i < j:
            MaxNum = min(height[i], height[j]) * (j - i)
            ans = max(MaxNum, ans)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))