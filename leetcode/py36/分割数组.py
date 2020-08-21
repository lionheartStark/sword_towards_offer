class Solution:

    def partitionDisjoint(self, A: list) -> int:
        N = len(A)
        maxleft = A[0]

        m = A[N - 1]
        minright = [None] * N
        for i in range(N - 1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in range(1, len(A)):
            maxleft = max(maxleft, A[i - 1])

            if maxleft <= minright[i]:
                return i

    def partitionDisjoint_best(self, A: list) -> int:
        """
        最好的划分办法
        """
        n = len(A)
        max_left = A[0]
        go_max = A[0]
        huafen = 1
        for i in range(1, n):
            if A[i] < max_left:
                huafen = i
                max_left = max(go_max, max_left)
            else:
                go_max = max(go_max, A[i])

        return huafen + 1


print(Solution().partitionDisjoint_best([5, 0, 3, 8, 6]))
