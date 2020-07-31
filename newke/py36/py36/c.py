from typing import List

import  math
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        if n <= 1:
            return 0
        else:
            sum_x, sum_y = 0,0
            for i in positions:
                sum_x += i[0]
                sum_y += i[1]
            x = sum_x / n
            y = sum_y / n

            res = 0
            for i in positions:
                a = (i[0] - x) ** 2 + (i[1] - y) ** 2
                res += math.sqrt(a)
            return res
print(Solution().getMinDistSum(positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]))