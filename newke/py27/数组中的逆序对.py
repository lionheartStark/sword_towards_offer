# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        if len(data) <= 1:
            return count
        for i in range(len(data)-1):
            if data[i+1]> data[i]:
                count+=1
        return count%1000000007