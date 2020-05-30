# -*- coding:utf-8 -*-
class Solution:
    def kClosest(self, points: list, K: int) -> list:
        a = lambda x :x[0]**2 + x[1]**2
        points.sort(key = a)
        return points[:K]
print(Solution().kClosest([[1,1],[1,2]],2))