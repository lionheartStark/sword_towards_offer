from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        hasset = set()

        A.sort()
        for i in A:
            hasset.add(i)
        n = len(A)
        if n == 0:
            return 0

        all = []
        for i in range(1, n):
            if A[i] == A[i - 1]:
                all.append(A[i])
        print(all)
        res = 0
        start = A[0]
        while all:
            if start in hasset:
                start += 1
            elif start > all[0]:
                res += start - all.pop(0)
                hasset.add(start)
            elif start < all[0]:
                start = all[0]
        return res

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        print(A)
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                res += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1

        return res


print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))
