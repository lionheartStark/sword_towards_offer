from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left_star = []

        for i in asteroids:
            if i > 0:
                left_star.append(i)
            else:
                iseq= False
                while left_star:
                    if left_star[-1] < 0:
                        left_star.append(i)
                        break
                    if left_star[-1] < -i:
                        left_star.pop()
                    elif left_star[-1] == -i:
                        left_star.pop()
                        iseq = True
                        break
                    else:
                        break
                if left_star == [] and not iseq:
                    left_star.append(i)

        return left_star

a = [5, 10, -5]
b = [8 ,-8]
res = Solution().asteroidCollision([-2,-2,1,-1])
print(res)