# -*- coding:utf-8 -*-
import copy
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum_n = [0]*(len(array)+1)
        for i in range(len(array)):
            sum_n[i+1] = sum_n[i]+array[i]
        max = 0
        for i in range(len(sum_n)):
            if i == 0:
                pass
            elif i == 1:
                max = sum_n[0]
            else:
                dd = copy.deepcopy(sum_n[:i])
                dd.sort()
                new = sum_n[i] - dd[0]
                max = new if new>max else max
        return max
print(Solution().FindGreatestSumOfSubArray([2,8,1,5,9]))