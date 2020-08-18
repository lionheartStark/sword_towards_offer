"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            aim_addr = nums[i]
            if i == aim_addr:
                continue
            if nums[aim_addr] == nums[i]:
                print(nums[i])
                return nums[i]
            nums[aim_addr], nums[i] = nums[i], nums[aim_addr]


Solution().findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
