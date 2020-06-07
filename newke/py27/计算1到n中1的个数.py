# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        str_n = str(n)
        if n ==1:
            return 1
        for i in range(len(str_n)):
            qianzhui = str_n[:i]
            houzhui = str_n[i+1:]
            #print(qianzhui, f",{str_n[i]},", houzhui)
            if str_n[i] == '0' :
                if houzhui:
                    res += int(houzhui)
                if qianzhui:
                    res += (int(qianzhui))* 10**(len(houzhui))
            elif int(str_n[i]) > 1:
                if houzhui:
                    houzhui = "9"*len(houzhui)
                res += int(qianzhui+houzhui)+1 if qianzhui or houzhui else 1
            else:
                if houzhui:
                    res += int(houzhui)+1
                if qianzhui:
                    res += (int(qianzhui)) * 10 ** (len(houzhui))

        #print(res)
        return res
Solution().NumberOf1Between1AndN_Solution(10)