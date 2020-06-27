class Solution:
    def maxSubarraySumCircular(self, A: list) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        sum_list = [0] * n
        sum_list[0] = A[0]
        for i in range(1, n):
            sum_list[i] = sum_list[i - 1] + A[i]

        minnum = min(0, sum_list[0])
        maxnum = sum_list[0]
        res = sum_list[0]
        fres = sum_list[0]
        for i in range(1, n):
            res = max(res, sum_list[i] - minnum)
            fres = min(fres, sum_list[i] - maxnum)
            minnum = min(minnum, sum_list[i])
            maxnum = max(maxnum, sum_list[i])
        return max(res, sum(A) - fres, sum(A))


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
