class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dpmap = {}
        dpmap[0] = 0
        dpmap[1] = 1
        dpmap[2] = 2
        if n <= 2:
            return dpmap[n]

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]