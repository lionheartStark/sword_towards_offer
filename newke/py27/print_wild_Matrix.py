# -*- coding:utf-8 -*-
class Solution:

    def printMatrix(self, matrix):
        """
        TODO：look
        pop()默认出去最后一个
        所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
        :param matrix:
        :return:
        """
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
a= [1,2,3]
print(a.pop())
print(a)
print (Solution().printMatrix([[1,2,3]]))