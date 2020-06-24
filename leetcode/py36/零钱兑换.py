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