from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_pre = nums[0]
        max_pre = nums[0]
        ans = max_pre

        for i in range(1, len(nums)):
            new_min_pre = min(nums[i] * min_pre, nums[i], nums[i] * max_pre)
            new_max_pre = max(nums[i] * min_pre, nums[i], nums[i] * max_pre)
            min_pre = new_min_pre
            max_pre = new_max_pre
            ans = max(ans, max_pre)
        return ans


ans = Solution().maxProduct([2, 3, -2, 4])
print(ans)
