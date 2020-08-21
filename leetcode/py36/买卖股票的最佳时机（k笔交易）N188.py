from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        限制卖出.超时
        """
        n = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        if k == 0 or n == 0:
            return 0

        for i in range(0, n):
            for j in range(0, k + 1):

                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = - prices[0]
                    continue
                elif j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = max(dp[i - 1][j][0] - prices[i], dp[i - 1][j][1])
                    continue
                # 未持有, 可能是发生了卖
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                # 有持有， 可能是发生了买
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])
        return dp[n - 1][k][0]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        限制买入
        """
        n = len(prices)
        if k == 0 or n == 0:
            return 0

        if k >= n // 2:
            # 此时可以任意交易不用在乎
            # dp = [[0, -prices[0]] for _ in range(n)]
            # for i in range(1, n):
            #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            #     # 有持有， 可能是发生了买
            #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # return int(dp[n - 1][0])
            pre = [0, -prices[0]]
            for i in range(1, n):
                now = [0, 0]
                now[0] = max(pre[0], pre[1] + prices[i])
                now[1] = max(pre[1], pre[0] - prices[i])
                pre = now
            return pre[0]


        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(0, n):
            for j in range(0, k + 1):

                if j == 0:
                    dp[i][0][0] = 0
                    dp[i][0][1] = - float('INF')
                    continue
                elif i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = - prices[i]
                    continue
                # 未持有, 可能是发生了卖
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # 有持有， 可能是发生了买
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return int(dp[n - 1][k][0])
