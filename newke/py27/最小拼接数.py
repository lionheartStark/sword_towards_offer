# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num=map(str,numbers)
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)