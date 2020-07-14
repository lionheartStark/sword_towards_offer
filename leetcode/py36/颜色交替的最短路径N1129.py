from typing import List
from collections import defaultdict
from copy import deepcopy


class Solution:

    def to_n_red_first(self, n, red_edges, blue_edges):
        queue = [(0, 0)]
        if 0 == n:
            return 0
        now_use = red_edges
        while queue:
            next = []
            while queue:
                i, step = queue.pop(0)
                should_rm = []
                for j in now_use[i]:
                    next.append((j, step + 1))
                    should_rm.append(j)
                    if j == n:
                        return step + 1
                now_use[i] = []
            queue = next
            if now_use == red_edges:
                now_use = blue_edges
            else:
                now_use = red_edges

        return -1

    def to_n_blue_first(self, n, red_edges, blue_edges):
        queue = [(0, 0)]
        if 0 == n:
            return 0
        now_use = blue_edges
        while queue:
            next = []
            while queue:
                i, step = queue.pop(0)
                should_rm = []
                for j in now_use[i]:
                    next.append((j, step + 1))
                    should_rm.append(j)
                    if j == n:
                        return step + 1
                now_use[i] = []
            queue = next
            if now_use == red_edges:
                now_use = blue_edges
            else:
                now_use = red_edges

        return -1

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:

        red_edges_dict = defaultdict(list)
        for i in red_edges:
            red_edges_dict[i[0]].append(i[1])

        blue_edges_dict = defaultdict(list)
        for i in blue_edges:
            blue_edges_dict[i[0]].append(i[1])
        res = []
        for i in range(n):
            red = self.to_n_red_first(i, deepcopy(red_edges_dict), deepcopy(blue_edges_dict))
            blue = self.to_n_blue_first(i, deepcopy(red_edges_dict), deepcopy(blue_edges_dict))
            res_this = None
            if red == -1 and blue == -1:
                res_this = -1
            elif red == -1:
                res_this = blue
            elif blue == -1:
                res_this = red
            else:
                res_this = min(red, blue)
            res.append(res_this)

        return res

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[
        int]:

        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for i, j in red_edges:
            red_graph[i].append(j)

        for i, j in blue_edges:
            blue_graph[i].append(j)

        # 第一个位置，第二颜色，第三个当前位置 (1:表示蓝色，2：表示红色，3表示当前步数)
        # 对于每一个元素，若是没有被处理，下一步可以走红色的路线，或者是蓝色的路线
        queue = [(0, 0, 0)]
        res = [-1] * n
        while queue:
            position, color, step = queue.pop(0)
            # 当前元素是1 蓝色，或者是没有被处理过
            if color == 1 or color == 0:
                for nextp in red_graph[position]:
                    queue.append((nextp, 2, step + 1))
                # 表示该节点已经被处理过了
                # 因为对于某条最短路，后到这个点的一定没有之前的快（最多持平）所以可以设置为空
                red_graph[position] = []
            if color == 2 or color == 0:
                for nextp in blue_graph[position]:
                    queue.append((nextp, 1, step + 1))
                blue_graph[position] = []
            # 由于第一个到达的就是最短的，所以只在-1的时候赋值
            if res[position] == -1:
                res[position] = step
        return res
