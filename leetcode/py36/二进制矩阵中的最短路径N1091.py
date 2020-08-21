from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if not grid or grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        if n <= 2:
            return n

        queue = [(0, 0, 1, [(0, 0)])]
        grid[0][0] = 2
        while queue:
            i, j, step, path = queue.pop(0)
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (1, 1), (0, 1), (1, 0), (1, -1), (-1, 1)]:
                x = i + dx
                y = j + dy
                if 0 <= x <= n - 1 and 0 <= y <= n - 1 and grid[x][y] == 0:
                    now_path = path + [(x, y)]
                    queue.append((x, y, step + 1, now_path))
                    grid[x][y] = 2
                    if x == n - 1 and y == n - 1:
                        print(now_path)
                        return step + 1
        return -1


queue = [(0, 0, 1, [(0, 0)])]
i, j, step, path = queue[0]
path.append((1, 1))
print(queue)

print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
