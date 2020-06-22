class Solution:
    def minimumTotal(self, triangle: list) -> int:
        dp = []
        dp.append([triangle[0][0]])
        for i in range(1, len(triangle)):
            this_layer_dp = []
            for j in range(len(triangle[i])):
                # 状态转移
                if j - 1 < 0:
                    now = dp[i - 1][j] + triangle[i][j]
                elif j >= len(dp[i - 1]):
                    now = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    now = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                this_layer_dp.append(now)
            dp.append(this_layer_dp)
        return min(dp[-1])


test_case = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(test_case))
