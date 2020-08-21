"""
给定一个字符串S和一个字符串T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 定义dp[i][j] 用s前i个可以凑出t前j个的个数
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for j in range(len_t + 1)] for i in range(len_s + 1)]

        for i in range(len_s + 1):
            dp[i][0] = 1

        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


ans = Solution().numDistinct("rabbbit", "rabbit")
print(ans)
