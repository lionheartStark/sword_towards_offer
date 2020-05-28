# -*- coding:utf-8 -*-
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A) + 1)]  # s代表前缀和，即s[i]表示sum(A[:i])
        kcnt = [0 for i in range(K)]  # kcnt[i]代表s中有多少个元素 mod K 为i
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
        # print s, kcnt

        return sum(x * (x - 1) // 2 for x in kcnt)

    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A)+1)]
        for i in range(len(s)):
            s[i+1] = s[i]+A[i]
        kcnt = [0 for i in range(K)]
        for i in s:
            kcnt[i%K]+=1

        return sum(x * (x - 1) // 2 for x in kcnt)
kcnt =  [2, 0, 1, 0, 4]
print(sum(x * (x - 1) // 2 for x in kcnt))