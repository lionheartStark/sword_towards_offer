class Solution:
    def beg(self, cap, N, wt, val):
        dp = [[0 for j in range(cap + 1)] for i in range(N+1)]
        # 在第i个包处，包总容量w个容量情况下可以装的最多的价值
        for i in range(1, N+1):
            for j in range(1, cap+1):
                if j >= wt[i-1]:
                    dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][cap]

    def canPartition(self, nums: list) -> bool:
        the_sum = sum(nums)
        if the_sum % 2 != 0:
            return False
        else:
            cap = the_sum // 2
            N = len(nums)

            dp = [[False for i in range(cap + 1)] for n in range(N + 1)]

            for n in range(N + 1):
                dp[n][0] = True

            for i in range(1, N + 1):
                for j in range(1, cap + 1):
                    if j >= nums[i - 1]:
                        dp[i][j] = (dp[i - 1][j]) | (dp[i - 1][j - nums[i - 1]])
                    else:
                        dp[i][j] = dp[i - 1][j]

            return dp[N][cap]

