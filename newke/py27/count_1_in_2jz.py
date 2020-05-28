# -*- coding:utf-8 -*-
class Solution:

    def NumberOf1(self, n):
        """
        输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
        :param n:
        :return:
        """

        def get_fan(n):
            return (n&0)
        # write code here
        if n >= 0:
            n = bin(n)
        else:
            n = str(bin(n))
            n = n[n.index("0b")+2:]
            if len(n) < 31:
                n = "0"*(31-len(n))+n
            new = ""
            for i in n:
                new += ("1" if int(i)==0 else "0")
            new = str(bin(int(new, 2)+1))
            new = new[new.index("0b") + 2:]
            if len(new) < 31:
                new = "0"*(31-len(new))+new
            knew = new[len(new)-31:]
            n = "1"+knew
        return n.count("1")

    def NumberOf12(self, num):
        if num >= 0:
            nbin = bin(num)
            return nbin.count('1')
        else:
            num = abs(num)
            nbin = bin(num - 1)
            return 32 - nbin.count('1')


Solution().NumberOf1(-2147483648)