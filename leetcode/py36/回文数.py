class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if not x[i] == x[len(x)-i-1]:
                return False
        return True

print(Solution().isPalindrome(1))