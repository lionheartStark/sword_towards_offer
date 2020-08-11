from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        x, y = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= x or j < 0 or j >= y:
                return
            if board[i][j] != "O":
                return
            else:
                board[i][j] = "@"
                dfs(i + 1, j)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)

        for i in range(0, x):
            if i == 0 or i == x - 1:
                for j in range(0, y):
                    dfs(i, j)
            else:
                for j in [0, y - 1]:
                    dfs(i, j)
        for i in range(x):
            for j in range(y):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "@":
                    board[i][j] = "O"
