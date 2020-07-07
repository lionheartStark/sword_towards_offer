from typing import List


class Solution:

    def run_fastest_dfs(self, i, j, grid):
        if i in [-1, self.xlen] or j in [-1, self.ylen]:
            print("越界", i, j)
            return
        elif grid[i][j] != '1':
            return
        else:
            grid[i][j] = '2'
            # shang
            self.run_fastest_dfs(i - 1, j, grid)
            # xia
            self.run_fastest_dfs(i + 1, j, grid)
            # zuo
            self.run_fastest_dfs(i, j - 1, grid)
            # you
            self.run_fastest_dfs(i, j + 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        self.ylen = len(grid[0])
        self.xlen = len(grid)
        res = 0
        for i in range(self.xlen):
            for j in range(self.ylen):
                if grid[i][j] == '1':
                    self.run_fastest_dfs(i, j, grid)
                    res += 1
        return res


a = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

print(Solution().numIslands(a))
