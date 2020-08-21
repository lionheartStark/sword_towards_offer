class Solution:
    def maxScoreSightseeingPair1(self, A: list) -> int:
        max = -1
        for i in range(len(A) - 1):

            for j in range(i + 1, len(A)):
                print(i, j)
                fen = A[i] + A[j] + i - j
                if fen > max:
                    max = fen
        print(max)
        return max

    def maxScoreSightseeingPairbest(self, A: list) -> int:
        ans, Ai_i = 0, A[0]  # Ai_i == max{0<=i<j |(A[i]+i) }
        for j, a in enumerate(A[1:], 1):  # j ∈ [1,A.length)
            ans = max(ans, Ai_i + a - j)  # (A[i]+i)+(A[j]-j)
            Ai_i = max(Ai_i, a + j)  # Update (A[i]+i) to keep max.
        return ans

    def maxScoreSightseeingPair(self, A: list) -> int:
        """
        而对于输入中的每一个 A[j] 来说， 它的值 A[j] 和它的下标 j 都是固定的，

        所以 A[j] - j 的值也是固定的。

        因此，对于每个 A[j] 而言， 想要求 res 的最大值，也就是要求 A[i] + i （i < j） 的最大值，

        所以不妨用一个变量 pre_max 记录当前元素 A[j] 之前的 A[i] + i 的最大值，

        这样对于每个 A[j] 来说，都有 最大得分 = pre_max + A[j] - j，

        再从所有 A[j] 的最大得分里挑出最大值返回即可。
        """
        ans, Ai_i = 0, A[0]
        for j in range(1, len(A)):
            ans = max(ans, Ai_i + A[j] - j)
            Ai_i = max(Ai_i, A[j] + j)
        return ans


a = [8, 1, 5, 2, 6]

Solution().maxScoreSightseeingPair(a)
