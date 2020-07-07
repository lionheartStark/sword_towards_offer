class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = list(num)
        n = len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(num))

        res = ""
        while k > 0 and num:
            want = min(num[0:k+1]) if k+1 <= n else min(num)
            find_idx = num.index(want)
            res = res + want
            #
            num.pop(find_idx)

            k -= find_idx


        for i in num:
            res = res + i
        return res




print(Solution().minInteger_use_dict(num = "4321", k = 4))
