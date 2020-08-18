from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = [0 for i in range(n)]
        min_val = float('INF')
        for i in range(n):
            if i == 0:
                sum_n[i] = nums[i]
            else:
                sum_n[i] = nums[i] + sum_n[i - 1]
            min_val = min(sum_n[i], min_val)

        x = 1 - min_val
        if x > 0:
            return x
        else:
            return 1


nums = [-3, 2, -3, 4, 2]
print(Solution().minStartValue(nums))
