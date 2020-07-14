import bisect
from typing import List


def my_bisect_left(a_list, x):
    lo = 0
    hi = len(a_list)

    while lo < hi:
        mid = (lo + hi) // 2
        if x > a_list[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo


class mySolution:
    def my_countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_list = []
        count_list = []

        for i in range(n - 1, - 1, -1):
            idx = my_bisect_left(sorted_list, nums[i])
            sorted_list.insert(idx, nums[i])
            count_list.insert(0, idx)
        return count_list

# 数状数组
class BIT:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def lowbit(self, i):
        return i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.arr[i]
            i -= self.lowbit(i)
        return s

    def update(self, i, delta):
        while i <= self.n:
            self.arr[i] += delta
            i += self.lowbit(i)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # BIT O(nlogn)
        n = len(nums)
        sortn = sorted(nums)  # 对nums进行排序，方便离散化后找到对应索引 O(nlogn)
        ans = []

        def discrete(x):
            return bisect.bisect(sortn, x)  # 二分查找索引 O(logn)

        bit = BIT(n)
        for i in range(n - 1, -1, -1):
            idx = discrete(nums[i])
            cnt = bit.query(idx - 1)  # O(logn)
            ans.append(cnt)
            bit.update(idx, 1)  # O(logn)
        return reversed(ans)


print(Solution().countSmaller([5, 2, 6, 1]))
