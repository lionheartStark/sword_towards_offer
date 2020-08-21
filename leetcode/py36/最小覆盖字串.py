from collections import defaultdict, Counter


class Solution:
    def has_sub(self, now_str, sub_count, now_count):
        # print(now_count)
        for k in sub_count:
            if sub_count[k] > now_count[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        i = 0
        j = 0
        now_str = ""
        res = (n + 1, "")
        while j < n:
            now_str = now_str + s[j]
            while self.has_sub(now_str, t):
                if len(now_str) < res[0]:
                    res = (len(now_str), now_str)
                now_str = now_str[1:]
                i += 1
            j += 1
        return res[1]

    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        i = 0
        j = 1
        res = (n + 1, "")
        now_count = defaultdict(int)
        sub_count = Counter(t)
        while j <= n:
            now_count[s[j - 1]] += 1
            now_str = s[i:j]
            while self.has_sub(now_str, sub_count, now_count):
                if len(now_str) < res[0]:
                    res = (len(now_str), now_str)
                now_count[s[i]] -= 1
                i += 1
                now_str = s[i:j]
            j += 1
        return res[1]


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))
