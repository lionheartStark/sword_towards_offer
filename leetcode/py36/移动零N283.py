from typing import List


class Solution:
    def maopao_moveZeroes(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] == 0:
                    nums[j] = nums[j + 1]
                    nums[j + 1] = 0

        return nums

    def moveZeroes(self, nums: List[int]):
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < n:
            nums[j] = 0
            j += 1
        return nums


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
