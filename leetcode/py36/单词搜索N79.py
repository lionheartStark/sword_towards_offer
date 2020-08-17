from typing import List


class Solution:

    def dfs(self, board, i, j, word):
        if word == "":
            return True
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            if board[i][j] == word[0]:
                board[i][j] = "@"

                for x, y in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                    if self.dfs(board, x, y, word[1:]):
                        return True
                board[i][j] = word[0]
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(board)
        y = len(board[0])

        for i in range(x):
            for j in range(y):
                if self.dfs(board, i, j, word):
                    return True
        return False
