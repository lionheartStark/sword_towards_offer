class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mem = {}

        def dp(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            else:
                # i<j
                print(s[i], s[j])
                if f"{i}, {j}" in mem:
                    return mem[f"{i}, {j}"]
                else:
                    if s[i] == s[j]:
                        mem[f"{i}, {j}"] = dp(i + 1, j - 1) + 2
                    else:
                        l = dp(i + 1, j)
                        r = dp(i, j - 1)
                        mem[f"{i}, {j}"] = max(l, r)
                    return mem[f"{i}, {j}"]

        res = dp(0, len(s) - 1)
        return res


print(Solution().longestPalindromeSubseq("ababaz"))
