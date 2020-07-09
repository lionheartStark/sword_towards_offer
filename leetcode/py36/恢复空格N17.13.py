from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n = len(sentence)
        dictionary = set(dictionary)
        if sentence == '':
            return 0

        dp = [0 for i in range(0, n + 1)]

        dp[0] = 0
        for i in range(1, n+1):
            find = dp[i-1]+1
            for words in dictionary:
                if sentence[:i].endswith(words):
                    print(sentence[:i])
                    find = min(find, dp[i-len(words)])

            dp[i] = find
        return dp[n]
dictionary =["potimzz"]
sentence = "potimzzpotimzz"

print(Solution().respace(dictionary,
sentence ))
