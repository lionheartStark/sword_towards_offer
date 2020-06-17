# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        xpy= range(n)
        lastidx = 0
        while len(xpy) != 1:
            lastidx = (m-1+lastidx) % (len(xpy))
            print(xpy.pop(lastidx))


Solution().LastRemaining_Solution(5,3)