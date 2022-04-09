from typing import List
class Solution:
    def trap(self, height: List[int]) -> int :
        leng = len(height)
        i = 0
        j = leng - 1
        leftMax = 0
        rightMax = 0
        ans = 0
        while i < j:
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])

            if height[i] < height[j]:
                ans += leftMax - height[i]
                i += 1
            else:
                ans += rightMax - height[j]
                j -= 1

        return ans
if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))