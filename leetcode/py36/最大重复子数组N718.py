class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_a = len(A)
        len_b = len(B)
        dp = [[0 for _ in range(len_b)] for _ in range(len_a)]

        for i in range(1, len_a):
            for j in range(1, len_b):
                if A[i] == B[j]:
                    dp[i][j]
