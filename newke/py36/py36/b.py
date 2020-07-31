class Solution:
    def numSub(self, s: str) -> int:
        s_list = s.split("0")
        ans_map = {}
        res = 0
        for i in s_list:
            n = len(i)
            if n in ans_map:
                res += ans_map[n]
            else:
                ans = (1+n)*n//2
                res += ans
                ans_map[n] = ans
        return res % (10**9 + 7)

print(Solution().numSub("111111"))