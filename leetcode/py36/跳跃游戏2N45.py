from typing import List


class Solution:
    def my_jump(self, nums: List[int]) -> int:
        n = len(nums)
        start_addr = 0
        step = 0

        if n == 1:
            return 0

        while True:
            fastest = 0
            next_move = None
            for can_move_long in range(1,  nums[start_addr]+1):
                nowfastest = start_addr + can_move_long + nums[start_addr + can_move_long]
                if start_addr + can_move_long >= n - 1:
                    return step + 1
                if nowfastest > fastest:
                    fastest = nowfastest
                    next_move = start_addr + can_move_long
            start_addr = next_move
            step += 1
        return step

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        """
        在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，
        我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
        如果访问最后一个元素，在边界正好为最后一个位置的情况下，
        我们会增加一次「不必要的跳跃次数」，
        因此我们不必访问最后一个元素。
        """
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

print(Solution().jump([2,3,1,1,4]))