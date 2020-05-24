# -*- coding:utf-8 -*-
class Solution:
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。
    求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    """
    def jumpFloor(self, number):
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            fun_num = []*number
            fun_num.append(1)
            fun_num.append(2)
            for i in range(2, number):
                fun_num.append(fun_num[i-1]+fun_num[i-2])
            return fun_num[number-1]