from typing import List
from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        map_count = defaultdict(int)

        for i in arr:
            map_count[i] += 1

        a2 = sorted(map_count.values())
        count = 0

        for i in a2:
            val = i[1]
            if k >= val:
                count += 1
                k -= val
            else:
                break
        return len(a2)-count

    def findLeastNumOfUniqueInts1(self, arr: List[int], k: int) -> int:
        import collections
        count_list = collections.Counter(arr)
        sort_val = sorted(count_list.values())
        for index, val in enumerate(sort_val):
            if k >= val:
                k = k - val
            else:
                return len(sort_val) - index
        return 0

print(Solution().findLeastNumOfUniqueInts(arr = [2,1,1,3,3,3], k = 3))