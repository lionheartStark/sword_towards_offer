class Solution:
    def change(self, amount: int, coins: list) -> int:
        len_coin = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(len_coin + 1)]
        # dp i,j 表示用前i个凑满j的办法数量

        # 凑0我们是总有办法的
        for i in range(len_coin + 1):
            dp[i][0] = 1

        for i in range(1, len_coin + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # 不用这一个+用这一个
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    # 只能不用这一个
                    dp[i][j] = dp[i - 1][j]

        return dp[len_coin][amount]

    def change2(self, amount: int, coins: list) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                # 在原基础上加上一个此类coin
                dp[x] += dp[x - coin]
        return dp[amount]




print(Solution().change(5, [1, 2, 5]))
