from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> List:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] > nums[i-1]:
                small_num = nums[i-1]
                for j in range(i, n):
                    if nums[j] > small_num:
                        pass
                    else:
                        j -= 1
                        nums[i-1] = nums[j]
                        nums[j] = small_num
                        nums = nums[0:i] + nums[i:][::-1]
                        return nums
                nums[i-1] = nums[j]
                nums[j] = small_num
                nums = nums[0:i] + nums[i:][::-1]
                return nums
        nums = nums[::-1]
        return nums

print(Solution().nextPermutation([1,3,2]))