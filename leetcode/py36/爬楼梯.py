# 还是DP，只不过是只存储前两个元素，减少了空间，空间复杂度O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2: return n
        a, b, temp = 1, 2, 0
        for i in range(3, n+1):
            temp = a + b
            a = b
            b = temp
        return temp

