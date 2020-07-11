from typing import List


class Solution:
    def maxProfitmy(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = - prices[0]

        dp[1][0] = max(dp[0][1] + prices[1], dp[0][0])
        dp[1][1] = max(dp[0][0] - prices[1], dp[0][1])
        for i in range(2, n):
            # 不持有
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            # 持有
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])

            pass
        return dp[n - 1][0]

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + \
            [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])


print(Solution().maxProfit([2, 1, 4]))
