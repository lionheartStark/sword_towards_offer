class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordDict = set(wordDict)
        self.res = False

        dp = [False] * (len(s) + 1)

        dp[0] = True
        for i in range(1, len(dp)):
            dp[i] = False
            for n in range(0, i):
                if dp[n] and s[n:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
