import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.findall(p, s)
        if len(res) >= 1:
            return s == res[0]
        else:
            return False


print(Solution().isMatch("aa", "a*"))
