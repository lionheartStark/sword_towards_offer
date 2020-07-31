from typing import List
from collections import  defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        to_map = defaultdict(dict)
        for i in range(len(edges)):
            to_map[edges[i][0]][edges[i][1]] = succProb[i]
            to_map[edges[i][1]][edges[i][0]] = succProb[i]

        dp = [0 for _ in range(n)]

        dp[start] = 1

        passed = {start}
        def kuo(i):
            to = to_map[i]
            need = []
            for k, v in to.items():
                
                if dp[i] * v > dp[k]:
                    dp[k] = dp[i] * v
                    need.append(k)
            for m in need:
                kuo(m)
        # for i in range(0, n):
        #     to = to_map[i]
        #     for k, v in to.items():
        #         dp[k] = max(dp[k], dp[i]*v)
        kuo(start)
        import pprint
        pprint.pprint(dp)
        return dp[end]

Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)