class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i = len(word1) + 1
        j = len(word2) + 1

        dp = [[0] * j for b in range(i)]

        # 初始化完毕
        for x in range(i):
            for y in range(j):
                if x == 0:
                    dp[x][y] = y
                elif y == 0:
                    dp[x][y] = x

        # 开始递推
        for x in range(1, i):
            for y in range(1, j):
                if word1[x - 1] == word2[y - 1]:
                    dp[x][y] = dp[x - 1][y - 1]
                else:
                    dp[x][y] = 1 + min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1])

        return dp[i - 1][j - 1]


print(Solution().minDistance("horse", "ros"))
