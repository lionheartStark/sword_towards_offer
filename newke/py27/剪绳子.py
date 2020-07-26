# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.zuiyoujie = {1:1, 2:2, 3:3, 4:4}


    def cutRope(self, number):
        
        # write code here
        if number <= 2:
            return 1
        elif number ==3:
            return 2
        elif number ==4:
            return 4
        amax = 0
        for i in range(1, number):

            if number-i in self.zuiyoujie:
                zuiyou = self.zuiyoujie[number-i]
            else:
                zuiyou = self.cutRope(number-i)
            tmp = i*zuiyou
            if tmp > amax:
                amax = tmp
        self.zuiyoujie[number] = amax
        return amax


print(Solution().cutRope(8))