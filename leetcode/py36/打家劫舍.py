class Solution(object):
    """
    不可以抢相邻
    """

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        if n == 0:
            return 0
        if n <= 2:
            return dp[n]

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


print(Solution().rob([1, 2, 3, 1]))
