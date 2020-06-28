from collections import defaultdict
class Solution:
    def canArrange(self, arr: list, k: int) -> bool:
        for i in range(len(arr)):
            arr[i] %= k

        kmap = defaultdict(int)

        for i in range(len(arr)):
            now = arr[i]
            kmap[now] += 1

        for key in kmap:
            if key == 0:
                if kmap[key] % 2 != 0:
                    return False
            else:
                if kmap[key] != kmap[k-key]:
                    return False
        return True

print(Solution().canArrange([-1,1,-2,2,-3,3,-4,4], k = 3))

