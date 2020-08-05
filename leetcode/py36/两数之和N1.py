from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {}
        for i in range(len(nums)):
            if target - nums[i] in val_map:
                return [val_map[target - nums[i]], i]
            val_map[nums[i]] = i


ans = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
print(ans)
