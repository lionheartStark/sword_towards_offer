from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        amount = target
        coins = candidates

        len_coin = len(coins)
        # 一开始解决方案都是空数组[]
        dp = [[[] for j in range(amount + 1)] for i in range(len_coin + 1)]
        # dp i,j 表示用前i个凑满j的办法数量

        # 凑0我们是总有办法的
        for i in range(len_coin + 1):
            dp[i][0] = [[]]

        for i in range(1, len_coin + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # 不用这一个+用这一个
                    dp[i][j] = dp[i - 1][j] + [(x + [coins[i - 1]]) for x in dp[i][j - coins[i - 1]]]
                else:
                    # 只能不用这一个
                    dp[i][j] = dp[i - 1][j]

        return dp[len_coin][amount]


print(Solution().combinationSum(candidates = [2,3,5], target = 8,))
