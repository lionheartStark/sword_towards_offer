from typing import List

"""
求全部递增的子序列
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(i, cur):
            if len(cur) > 1:
                res.add(cur)
            if i >= len(nums):
                return
            if not cur or cur[-1] <= nums[i]:
                dfs(i + 1, cur + (nums[i],))
            dfs(i + 1, cur)

        dfs(0, ())
        return [list(i) for i in res]
