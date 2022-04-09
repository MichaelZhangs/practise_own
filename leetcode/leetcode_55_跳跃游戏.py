from typing import List
class Solution:
    def jump(self, nums: List[int])->int :
        leng = len(nums)
        k = 0
        for i in range(leng):
            print(k)
            if i > k:
                return False
            if k >= leng -1:
                return True
            k = max(k, nums[i] + i)
        return True

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    # nums = [3, 2, 1, 0, 4]
    print(Solution().jump(nums))