from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        只交易一次
        """
        res = 0
        n = len(prices)
        if n <= 1:
            return 0
        minpre = prices[0]

        for i in range(1, n):
            res = max(prices[i] - minpre, res)
            minpre = min(prices[i], minpre)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        """
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        """
        res = 0
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for i in range(2)] for j in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[n-1][0]
