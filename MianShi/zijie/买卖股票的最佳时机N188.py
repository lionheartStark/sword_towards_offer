from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n == 0:
            return 0

        if k >= n // 2:
            pre = [0, -prices[0]]
            for i in range(1, n):
                now = [0, 0]
                now[0] = max(pre[0], pre[1] + prices[i])
                now[1] = max(pre[1], pre[0] - prices[i])
                pre = now
            return pre[0]

        dp = [[[0, 0] for i in range(k+1)] for j in range(n)]

        for i in range(0, n):
            for j in range(0, k+1):
                if j == 0:
                    dp[i][0][0] = 0
                    dp[i][0][1] = - float('INF')
                    continue
                elif i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = - prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return int(dp[n - 1][k][0])
