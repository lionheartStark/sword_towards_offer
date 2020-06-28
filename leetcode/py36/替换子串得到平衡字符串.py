# -*- coding:utf-8 -*-

class Solution:
    def find_it(self, now, want):
        for k in want:
            if want[k] > now[k]:
                return False
        return True

    def balancedString(self, s: str) -> int:
        res = len(s)
        meige = len(s) // 4
        want_map = {}
        for key in ["Q", "W", "E", "R"]:
            count = s.count(key)
            if count - meige > 0:
                want_map[key] = count - meige
        if not want_map:
            return 0

        i = 0
        j = 1
        now_str = {"Q": 0, "W": 0, "E": 0, "R": 0}
        now_str[s[i]] += 1
        now_len = 1
        while i < j and j < len(s):
            while j < len(s) and not self.find_it(now_str, want_map):
                now_str[s[j]] += 1
                j += 1
                now_len += 1
            while i < j and self.find_it(now_str, want_map):
                res = min(now_len, res)
                now_str[s[i]] -= 1
                i += 1
                now_len -= 1
        return res


s = "WWEERQQQ"
print(s[0:1])
print(Solution().balancedString(s))
