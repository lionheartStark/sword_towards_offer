class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = ''
        if num1 == '0' or num2 == '0':
            return '0'
        lastsum = 0
        for lastnum in num2[::-1]:
            nowji = int(num1) * int(lastnum)
            nowsum = nowji+lastsum
            res = f"{nowsum%10}" + res
            lastsum = (nowsum - nowsum % 10) // 10
        if lastsum != 0:
            res = str(lastsum) + res
        else:
            pass
        return res



print(Solution().multiply("666","777"))