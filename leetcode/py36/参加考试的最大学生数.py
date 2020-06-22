from collections import defaultdict


class Solution:

    def maxStudents(self, seats: list) -> int:

        self.hang = len(seats)
        self.lie = len(seats[0])
        self.randmap = defaultdict(int)

        def update_ix(i, j, seats):
            if seats[i][j] != ".":
                return
            self.randmap[f"{i},{j}"] = 0
            for m in [i - 1, i, i + 1]:
                for n in [j - 1, j, j + 1]:
                    if 0 <= m < self.hang and 0 <= n < self.lie and not (m == i and n == j):
                        if seats[m][n] == ".":
                            self.randmap[f"{i},{j}"] += 1

        i = 0
        j = 0

        while i < self.hang and j < self.lie:
            while j < self.lie:
                # 计算四周情况
                update_ix(i, j, seats)
                j += 1
            i += 1
            j = 0

        print('ORIGIN ', self.randmap)

        for count in range(8, 0, -1):
            should_pop = []
            for k, v in self.randmap.items():
                if self.randmap[k] == count:
                    hang, lie = k.split(",")
                    i = int(hang)
                    j = int(lie)
                    for m in [i - 1, i, i + 1]:
                        for n in [j - 1, j, j + 1]:
                            if f"{m},{n}" in self.randmap:
                                self.randmap[f"{m},{n}"] -= 1
                    should_pop.append(k)
            [self.randmap.pop(k) for k in should_pop]
        print(f"res = {len(self.randmap)}, {self.randmap}")
        return len(self.randmap)


a = [[".", "#"], ["#", "#"], ["#", "."], ["#", "#"], [".", "#"]]
b = [["#", ".", "#", "#", ".", "#"], [".", "#", "#", "#", "#", "."], ["#", ".", "#", "#", ".", "#"]]
C = [["#", ".", ".", ".", "#"], [".", "#", ".", "#", "."], [".", ".", "#", ".", "."], [".", "#", ".", "#", "."],
     ["#", ".", ".", ".", "#"]]

Solution().maxStudents(C)
