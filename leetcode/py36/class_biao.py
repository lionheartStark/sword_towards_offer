from typing import List
from collections import defaultdict,deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        need_map = defaultdict(set)
        for i in prerequisites:
            need, be_need = i
            need_map[need].add(be_need)
        a_solution = []
        queue = deque()
        count = 0
        for i in range(numCourses):
            if i not in need_map:
                queue.append(i)
                count += 1
        while queue:
            nowican = queue.popleft()
            a_solution.append(nowican)
            should_rm = []
            for k, v in need_map.items():
                if nowican in v:
                    v.remove(nowican)
                    if len(v) == 0:
                        should_rm.append(k)
                        queue.append(k)
                        count += 1
            for m in should_rm:
                need_map.pop(m)

        can = (count == numCourses)
        if can:
            return a_solution
        else:
            return []


