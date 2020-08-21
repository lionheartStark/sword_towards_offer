"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for L in range(n):
            for i in range(n - L):
                j = i + L
                if L == 0:
                    dp[i][j] = 1
                elif L == 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
        ans = 0
        for i in dp:
            ans += sum(i)
        return ans


ans = Solution().countSubstrings("aaa")
print(ans)
