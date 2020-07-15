import heapq

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myheapq = []
        for i in nums:
            if len(myheapq) < k:
                heapq.heappush(myheapq, i)
            else:
                if i > myheapq[0]:
                    heapq.heappop(myheapq)
                    heapq.heappush(myheapq, i)

        return myheapq[0]


print(Solution().findKthLargest([3,2,1,5,6,4] , k = 2))