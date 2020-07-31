from typing import List
import bisect
from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sort_list = defaultdict(list)
        res = 0
        for i in nums:
            idx = bisect.bisect_right(sort_list[i],i)
            sort_list[i].insert(idx, i)
            res += idx
        return res
print(Solution().numIdenticalPairs(nums = [1,1,1,1]))