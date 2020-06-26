# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1

print(Solution().FirstNotRepeatingChar("aaaaaaaaabccccccc"))