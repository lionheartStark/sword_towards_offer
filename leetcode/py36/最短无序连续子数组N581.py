from typing import List

from typing import List


class Solution:
    def my_findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        shixu = []

        minx = float('INF')
        maxy = 0

        for i in range(n):
            if stack == [] or nums[i] >= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                j = 0
                while stack[j][0] <= nums[i]:
                    j += 1
                minx = min(minx, stack[j][1])
                maxy = i
        if minx != float('INF'):
            return -minx + maxy + 1
        else:
            return 0


a = Solution().findUnsortedSubarray([1, 3, 5, 2, 4])
print(a)
