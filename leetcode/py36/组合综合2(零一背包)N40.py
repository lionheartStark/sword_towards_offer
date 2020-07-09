from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        amount = target
        coins = candidates
        coins.sort()
        print(coins)
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
                    a = dp[i - 1][j]
                    b = [(x + [coins[i - 1]]) for x in dp[i-1][j - coins[i - 1]]]

                    dp[i][j] = a+b
                else:
                    # 只能不用这一个
                    dp[i][j] = dp[i - 1][j]
        res_dict = {}
        for i in dp[len_coin][target]:
            res_dict[str(i)] = i
        res = [v for k, v in res_dict.items()]
        return res



    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


print(Solution().combinationSum2(candidates = [1,2,2,2,5], target = 5,))