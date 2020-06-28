class Solution:
    def isPathCrossing(self, path: str) -> bool:
        now = (0, 0)
        passby = set()
        passby.add(now)
        for x in path:
            i, j = now
            if x == "N":
                now = (i + 1, j)
            elif x == "S":
                now = (i - 1, j)
            elif x == "E":
                now = (i, j + 1)
            elif x == "W":
                now = (i, j - 1)
            if now in passby:
                return True
            else:
                passby.add(now)
        return False


print(Solution().isPathCrossing("NESWW"))