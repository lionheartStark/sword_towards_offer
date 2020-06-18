class Solution:
    def __init__(self):
        self.count = 0

    def in_them(self, num, nowstr) -> int:
        if len(num) == 0:
            print(nowstr)
            self.count += 1
        elif len(num) == 1:
            nowstr.append(num)
            print(nowstr)
            self.count += 1
        else:
            self.in_them(num[1:], nowstr+[num[0:1]])
            if int(num[0:2])<= 25:
                self.in_them(num[2:], nowstr+[num[0:2]])
    def translateNum(self, num: int) -> int:
        self.in_them(str(num),[])
        return self.count

    def translateNum(self, num: int) -> int:
        string = str(num)
        dp = [0] * len(string)

        for i in range(len(string)):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1 + (1 if int(string[:2]) < 26 else 0)
            else:
                dp[i] = dp[i - 1] + (dp[i - 2] if 9 < int(string[i - 1:i + 1]) < 26 else 0)
        return dp[-1]
print(Solution().translateNum(12258))