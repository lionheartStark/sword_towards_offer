from typing import List
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tuzi_ans = Counter(answers)
        print(tuzi_ans)
        ans = 0
        for k,v in tuzi_ans.items():
            if v <= k+1:
                ans += k+1
            elif v > k+1:
                while v > k+1:
                    ans += k+1
                    v -= k + 1
                if v >0 and v <= k+1:
                    ans += k+1
        return ans


answers = [1,1,1,1]
ans = Solution().numRabbits(answers)
print(ans)