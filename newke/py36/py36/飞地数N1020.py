from typing import List
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])

        def dfs(i, j):
            A[i][j] = 0

            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < row and 0 <= y < col and A[x][y] == 1:
                    dfs(x, y)

        for i in range(row):
            if A[i][0] == 1:
                dfs(i, 0)
            if A[i][-1] == 1:
                dfs(i, col - 1)

        for j in range(col):
            if A[0][j] == 1:
                dfs(0, j)
            if A[row - 1][j] == 1:
                dfs(row - 1, j)

        return sum([sum(A[i]) for i in range(row)])