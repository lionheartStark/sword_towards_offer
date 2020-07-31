from typing import List
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        to_map = defaultdict(set)
        from_map = defaultdict(set)
        for afrom , ato in connections:
            to_map[afrom].add(ato)
            from_map[ato].add(afrom)

        sholud_be_to = [0]
        passed = set()
        res = 0
        while sholud_be_to:
            node = sholud_be_to.pop(0)

            passed.add(node)
            res += len(to_map[node] - passed)
            sholud_be_to.extend(list(to_map[node] - passed))
            sholud_be_to.extend(list(from_map[node] - passed))
        return res

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = set([0])
        count = 0
        while len(s) != n:
            for f, t in connections:
                if f in s:
                    count += 1
                    s.add(t)
                elif t in s:
                    s.add(f)
        return count

print(Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))