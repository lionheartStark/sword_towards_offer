class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        递归
        """
        lens = len(s)
        if len(s) == 0:
            return ""
        self.res = (1, (0, 0))
        dp = {}

        def dps(i, j):
            if i > j:
                return False
            elif i == j:
                return True
            elif (i, j) in dp:
                return dp[(i, j)]
            else:
                if i == j - 1:
                    now = s[i] == s[j]
                else:
                    now = dps(i + 1, j - 1) and s[i] == s[j]
                if now:
                    if j - i + 1 > self.res[0]:
                        self.res = (j - i + 1, (i, j))
                dp[(i, j)] = now
                return now

        for i in range(lens):
            for j in range(lens):
                if i > j:
                    continue
                dps(i, j)
        i, j = self.res[1]
        ans = s[i:j + 1]
        return ans


    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                print(i, j)
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])

                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans

Solution().longestPalindrome("abbccddeedfwrbgfiuwv")