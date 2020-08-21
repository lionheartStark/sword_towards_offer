from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        超时
        :param dungeon:
        :return:
        """
        lenx = len(dungeon)
        leny = len(dungeon[0])
        self.res = float('INF')
        memo = {}

        def dfs(x, y, life, sum_own):
            if sum_own >= self.res:
                return
            if x < 0 or x > lenx - 1 or y < 0 or y > leny - 1:
                return
            now_life = life + dungeon[x][y]
            # 如果命不够了就续上
            if now_life <= 0:
                sum_own += 1 - now_life
                now_life = 1
            # 如果到了目的地就上报欠债
            if x == lenx - 1 and y == leny - 1:
                self.res = min(self.res, sum_own)
            else:
                if (x + 1, y) in memo and sum_own >= memo[(x + 1, y)]:
                    pass
                else:
                    dfs(x + 1, y, now_life, sum_own)
                    memo[(x + 1, y)] = sum_own

                if (x, y + 1) in memo and sum_own >= memo[(x, y + 1)]:
                    pass
                else:
                    dfs(x, y + 1, now_life, sum_own)
                    memo[(x, y + 1)] = sum_own

        # queue = []
        # while queue:
        #     x, y, life, sum_own = queue.pop(0)
        #     if sum_own >= self.res:
        #         continue
        #     if x < 0 or x > lenx - 1 or y < 0 or y > leny - 1:
        #         continue
        #     now_life = life + dungeon[x][y]
        #     # 如果命不够了就续上
        #     if now_life <= 0:
        #         sum_own += 1 - now_life
        #         now_life = 1
        #     # 如果到了目的地就上报欠债
        #     if x == lenx - 1 and y == leny - 1:
        #         self.res = min(self.res, sum_own)
        #     else:
        #         queue.append((x + 1, y, now_life, sum_own))
        #         queue.append((x, y + 1, now_life, sum_own))

        dfs(0, 0, 1, 0)
        return 1 + self.res


a = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]
print(Solution().calculateMinimumHP(a))
