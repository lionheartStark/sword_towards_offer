class Solution:
    def has_sub(self, now_str, sub_str):
        for i in sub_str:
            if sub_str.count(i) > now_str.count(i):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        i = 0
        j = 0
        now_str = ""
        res = (n+1, "")
        while j < n:
            now_str = now_str + s[j]
            while self.has_sub(now_str, t):
                if len(now_str) < res[0]:
                    res = (len(now_str), now_str)
                now_str = now_str[1:]
                i += 1
            j += 1
        return res[1]
print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))