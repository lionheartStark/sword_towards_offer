from typing import List
class Solution:

    def sheng(self, index, num, rating):
        if num == 3:
            return 1
        if index == self.n-1 and num != 3:
            return 0
        else:
            res = 0
            for i in range(index+1, self.n):
                if rating[i] > rating[index]:
                    res += self.sheng(i, num+1, rating)
            return res

    def jiang(self, index, num, rating):
        if num == 3:
            return 1
        if index == self.n - 1 and num != 3:
            return 0
        else:
            res = 0
            for i in range(index + 1, self.n):
                if rating[i] < rating[index]:
                    res += self.jiang(i, num + 1, rating)
            return res



    def numTeams(self, rating: List[int]) -> int:
        self.n = len(rating)
        res = 0
        for i in range(len(rating)):
            sheng = self.sheng(i, 1, rating)
            jiang = self.jiang(i, 1, rating)
            print(i, rating[i], sheng, jiang)
            res += sheng+jiang
        return res


    def numTeams(self, rating: List[int]) -> int:
        """
        枚举中间数
        """
        n = len(rating)
        ans = 0
        # 枚举三元组中的 j
        for j in range(1, n - 1):
            iless = imore = kless = kmore = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    iless += 1
                # 注意这里不能直接写成 else
                # 因为可能有评分相同的情况
                elif rating[i] > rating[j]:
                    imore += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    kless += 1
                elif rating[k] > rating[j]:
                    kmore += 1
            ans += iless * kmore + imore * kless
        return ans


print(Solution().numTeams(rating = [2,5,3,4,1]))