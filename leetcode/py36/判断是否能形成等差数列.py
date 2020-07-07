from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)

        if n <= 2:
            return True
        arr.sort()

        cha = arr[1] - arr[0]
        for i in range(2, len(arr)):
            now_cha = arr[i] - arr[i - 1]
            if now_cha != cha:
                return False
        return True

print(Solution().canMakeArithmeticProgression([1,2,4]))