from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        last = 1
        max_len = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                last = last + 1
                max_len = max(last, max_len)
            else:
                last = 1
        return max_len



print(Solution().findLengthOfLCIS([1,3,5,4,7]))