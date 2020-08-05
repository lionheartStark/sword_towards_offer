class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""

        # 左闭合右闭合 dp[i][j]
        # 枚举子串的长度 l+1
        for the_long in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                # i是起始位置
                j = i + the_long
                # 越界返回
                if j >= len(s):
                    break
                # 是自己，当然回文
                if the_long == 0:
                    dp[i][j] = True
                # 长度为1则有两个数，直接判等
                elif the_long == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    # 利用上次的结果
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and the_long + 1 > len(ans):
                    ans = s[i:j+1]
        return len(ans)

