# -*- coding:utf-8 -*-

import bisect
class Solution:
    """
    子数组=>想到双指针
    """

    def minSubArrayLen_2fen(self, s: int, nums: list) -> int:
        """
        使用2分方法也可以做出来，对的
        """

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        # 不能忽略全部和的情况
        nums.insert(0, 0)
        print(nums)
        n = len(nums)
        res = float("INF")

        # 得到前缀和
        for i in range(len(nums)):
            x = s + nums[i]
            idx = bisect.bisect_left(nums, x)
            print(i, x, idx)
            if idx == n:
                continue
            else:
                len_of_this = idx - i
                res = min(res, len_of_this)
        return int(res) if res != float("INF") else 0



    def minSubArrayLen_my2p(self, s, nums):
        """
        [i,j],对的
        """
        i = 0
        j = 0
        n = len(nums)
        if n == 0:
            return 0
        sum_now = 0
        res = float("INF")
        while j < n:
            sum_now += nums[j]
            while sum_now >= s:
                res = min(res, j-i+1)
                sum_now -= nums[i]
                i += 1
            j += 1
        return res if res != float("INF") else 0

print(Solution().minSubArrayLen_2fen(7, [2, 3, 1, 2, 4, 3]))
