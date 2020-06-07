# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        useful = numbers.count(0)
        themax = max(numbers)
        if max(numbers)+useful<5:
            return False
        want = set(range(themax-5+1, themax+1))
        get = set(numbers)
        get -= {0}
        loss = want - get
        if len(loss) <= useful:
            return True
        else:
            themax = max(numbers)+useful
            want = set(range(themax - 5 + 1, themax + 1))

            loss = want - get
            if len(loss) <= useful:
                return True
            else:
                return False
a = [1,2,3,0,0]
print Solution().IsContinuous(a)
