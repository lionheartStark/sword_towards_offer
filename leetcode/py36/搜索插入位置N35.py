from typing import List


class Solution:
    def fen2_left(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.fen2_left(nums, target)
