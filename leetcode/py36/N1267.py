from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        count_x, count_y = [0] * x, [0] * y
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    count_x[i] += 1
                    count_y[j] += 1
        ans = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1 and (count_x[i] > 1 or count_y[j] > 1):
                    ans += 1
        return ans
