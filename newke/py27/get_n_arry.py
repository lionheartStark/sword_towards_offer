# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci_bad(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 3:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)

    def Fibonacci(self, n):
        """
        减少一次计算量
        :param n:
        :return:
        """
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 3:
            s = []*n
            s.append(1)
            s.append(1)
            for i in xrange(2,n):
                s.append(s[i-1]+s[i-2])
            return s[n-1]

print (Solution().Fibonacci(33))