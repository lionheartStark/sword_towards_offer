from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: list) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.lis([i[1] for i in envelopes])

    def lis(self, nums):
        dp = []
        max = []
        for i in range(len(nums)):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                max = dp[:] if len(max) < len(dp) else max
                dp[idx] = nums[i]
        max = dp[:] if len(max) < len(dp) else max
        print(max)
        return len(dp)


envelopes = [[7, 8], [12, 16], [12, 5], [1, 8], [4, 19], [3, 15], [4, 10], [9, 16]]
Solution().lis([5, 4, 2, 3, 4, 1, 0, 2, 3, 4, 1, 2])
