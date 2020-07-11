from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        给定一个非负整数数组，你最初位于数组的第一个位置。

        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        判断你是否能够到达最后一个位置。
        """
        n = len(nums)
        now_fast = 0
        for i in range(n):
            if i <= now_fast:
                now_fast = max(i + nums[i], now_fast)
            else:
                return False
        return True




print(Solution().canJump([3,2,1,0,4]))