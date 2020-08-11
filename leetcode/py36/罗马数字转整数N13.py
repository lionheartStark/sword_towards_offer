class Solution:
    def romanToInt(self, s: str) -> int:
        val_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, }
        count = 0
        n = len(s)
        ans = 0
        for i in range(n - 1, -1, -1):
            val = val_map[s[i]]
            if i + 1 <= n - 1 and val_map[s[i]] < val_map[s[i + 1]]:
                val = -val
            ans += val
        return ans


ans = Solution().romanToInt("IV")
print(ans)
