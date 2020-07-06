from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]: return 0
        # DP
        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    dp[i][j] = ((dp[i][j - 1] + 1) if j > 0 else 1)
                    mmin = float('inf')
                    for k in range(i, -1, -1):  # 从i开始遍历,到0结束, 计算能组成的矩阵个数
                        mmin = min(mmin, dp[k][j])
                        ans += mmin

                        # 提前结束循环
                        if mmin == 0:
                            break
        return ans