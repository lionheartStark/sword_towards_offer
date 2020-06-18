# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        1.为什么分三个队列？
        丑数数组里的数一定是有序的，因为我们是从丑数数组里的数乘以2,3,5选出的最小数，一定比以前未乘以2,3,5大。
        同时对于三个队列内部，按丑数数组里的先后顺序乘以2,3,5分别放入，一定比之前一个丑数未乘以2，3，5大；
        2.为什么比较三个队列头部最小的数放入丑数数组？
        因为三个队列是有序的，所以取出三个头中最小的，等同于找到了三个队列所有数中最小的。
        3.我们没有必要维护三个队列，只需要记录三个指针显示到达哪一步；“|”表示指针,arr表示丑数数组；
        :param index:
        :return:
        """
        # write code here
        chou_list = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        if index <= 0:
            return 0
        while len(chou_list) < index:
            new_chou = min(chou_list[idx2]*2, chou_list[idx3]*3, chou_list[idx5]*5)
            chou_list.append(new_chou)
            if chou_list[idx2]*2 == new_chou:
                idx2 += 1
            if chou_list[idx3]*3 == new_chou:
                idx3 += 1
            if chou_list[idx5]*5 == new_chou:
                idx5 += 1
        return chou_list[-1]

print(Solution().GetUglyNumber_Solution(5))