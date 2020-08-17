"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        len_s = len(s)
        dp = [0 for i in range(len_s + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        if s[0] == '0':
            return 0
        for i in range(2, len_s + 1):
            if s[i - 2] != '0' and 1 <= int(s[i - 2] + s[i - 1]) <= 26:
                if s[i - 1] != '0':
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 2]
            elif s[i - 1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


ans = Solution().numDecodings("100")
print(ans)