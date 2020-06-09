from collections import defaultdict


class Solution:
    """
    passed
    """
    def is_sub(self, s1, s2):
        for i in s1:
            if not s2[i] == s1[i]:
                return False
        else:
            return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
            window_len = len(s1)
            res = False

            standdict = defaultdict(int)
            for i in s1:
                standdict[i] += 1
            i = 0
            nowdict = defaultdict(int)
            while i + window_len <= len(s2):
                # 第一次初始化的时候
                if len(nowdict) == 0:
                    for m in s2[i:i + window_len]:
                        nowdict[m] += 1
                # 判别是不是子串
                print(nowdict)
                if self.is_sub(standdict, nowdict):
                    return True
                else:
                    nowdict[s2[i]] -= 1
                    if not i + window_len >= len(s2):
                        nowdict[s2[i + window_len]] += 1
                    i += 1

            return res
a = ("ab","eidbaooo")
b = ("ab", "eidboaoo")

print(Solution().checkInclusion(*a))