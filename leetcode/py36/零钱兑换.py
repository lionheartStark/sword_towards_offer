class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            else:
                if n == 0:
                    return 0
                elif n < 0:
                    return -1
                hasjie = False
                for coin in coins:
                    subp = dp(n - coin)
                    if subp >= 0:
                        if hasjie == False:
                            hasjie = True
                            res = 1 + subp
                        else:
                            res = min(res, 1 + subp)
                if hasjie:
                    memo[n] = res
                    return res
                else:
                    return -1

        return dp(amount)

    def coinChange(self, coins: list, amount: int) -> int:
        """
        make by self
        :param coins:
        :param amount:
        :return:
        """
        dp = [0]*(amount+1)
        dp[0] = 0

        for i in range(1, len(dp)):
            has_jie = False
            for coin in coins:

                qian = (i -coin)
                if qian >=0 and dp[qian]:

                    if has_jie == True:
                        dp[i] = min(dp[i],1+dp[qian])
                    else:
                        has_jie = True
                        dp[i] = 1+dp[qian]
            if has_jie == False:
                dp[i] = -1
        return dp[amount]