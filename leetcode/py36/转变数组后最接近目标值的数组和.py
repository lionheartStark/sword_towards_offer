# -*- coding:utf-8 -*-
class Solution:
    def findBestValue(self, arr: list, target: int) -> int:
        arr.sort()
        less_idx = -1
        for i in range(0, len(arr)):
            the_sum = sum(arr[0:i]) + arr[i] * (len(arr)-i)
            if the_sum >= target:
                break
            else:
                less_idx = i

        if (len(arr) - less_idx - 1) == 0 :
            return arr[-1]
        elif less_idx < 0:
            a = target // len(arr)
        else:
            a = (target - sum(arr[0:less_idx + 1])) // (len(arr) - less_idx - 1)


        if a < arr[less_idx]:
            use_a = abs(a * (len(arr) - 0) - target)
        else:
            use_a = abs(sum(arr[0:less_idx+1]) + a * (len(arr)-less_idx-1) - target)

        b = a+1
        if b < arr[less_idx]:
            use_b = abs(b * (len(arr) - 0) - target)
        else:
            use_b = abs(sum(arr[0:less_idx+1]) + b * (len(arr)-1-less_idx) - target)

        if use_a <= use_b:
            return a
        else:
            return b


print(Solution().findBestValue([1547,83230,57084,93444,70879],71237))