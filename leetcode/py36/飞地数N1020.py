from typing import List


class Solution:

    def run_fastest_dfs(self, i, j, grid):
        if i in [-1, self.xlen] or j in [-1, self.ylen]:
            print("越界", i, j)
            return True
        elif grid[i][j] != '1':
            return False
        else:
            self.nums += 1
            grid[i][j] = '2'
            # shang
            a = self.run_fastest_dfs(i - 1, j, grid)
            # xia
            b = self.run_fastest_dfs(i + 1, j, grid)
            # zuo
            c = self.run_fastest_dfs(i, j - 1, grid)
            # you
            d = self.run_fastest_dfs(i, j + 1, grid)
            return a or b or c or d

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.ylen = len(grid[0])
        self.xlen = len(grid)
        res = 0
        for i in range(self.xlen):
            for j in range(self.ylen):
                self.nums = 0
                if grid[i][j] == '1':
                    if not self.run_fastest_dfs(i, j, grid):
                        res += self.nums
        return res


a = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

print(Solution().numIslands(a))
