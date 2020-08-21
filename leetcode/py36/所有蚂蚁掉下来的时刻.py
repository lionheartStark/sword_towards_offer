from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        p = left + right
        all = []
        for i in left:
            all.append(i)
        for j in right:
            all.append(n - j)
        return max(all)


print(Solution().getLastMoment(n=20, left=[4, 7, 5], right=[9, 3, 13, 10]))
