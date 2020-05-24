# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        """
        我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
        请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
        总共有多少种方法？
        :param number:
        :return:
        """
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            fun_num = [] * number
            fun_num.append(1)
            fun_num.append(2)
            for i in range(2, number):
                fun_num.append(fun_num[i - 1] + fun_num[i - 2])
            return fun_num[number - 1]
