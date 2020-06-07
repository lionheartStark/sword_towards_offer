# -*- coding:utf-8 -*-
import math
class Solution:
    """
    passed
    """
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        xian = int(math.sqrt(tsum*2))+1
        for n in range(2, xian):
            the_list = []
            if n % 2 == 1 and tsum % n == 0:
                the_list = list(range(tsum // n - n // 2, tsum // n)) + list(range(tsum // n, tsum // n + n // 2 + 1))
            elif n % 2 == 0 and (float(tsum)/n) % 1 == 0.5:
                the_list = list(range(tsum // n - n // 2 + 1, tsum // n)) + list(range(tsum // n, tsum // n + n // 2 + 1))
            if len(the_list) > 1:
                res.append(the_list)
        res.sort(key=lambda x: x[0])
        return res