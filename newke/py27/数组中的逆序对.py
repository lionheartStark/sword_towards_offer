# -*- coding:utf-8 -*-

import bisect


def find_idx(num, sorted_list):
    if sorted_list:
        if num <= sorted_list[len(sorted_list) // 2]:
            return 0 + find_idx(num, sorted_list[:len(sorted_list) // 2])
        elif num > sorted_list[len(sorted_list) // 2]:
            return len(sorted_list) // 2 + 1 + find_idx(num, sorted_list[len(sorted_list) // 2 + 1:])

    else:
        return 0


class Solution:
    """
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组,求出这个数组中的逆序对的总数P。
    并将P对1000000007取模的结果输出。
    即输出P%1000000007
    """

    def reversePairs(self, data):
        # write code here
        data = data[::-1]
        sorted_list = []
        count_list = []
        count = 0
        for i in data:
            # 得到的idx
            idx = bisect.bisect_left(sorted_list, i)
            # 计算count
            count += idx
            sorted_list.insert(idx, i)
        return count


b = [364, 637, 341]
a = [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360,
     965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162, 268, 142,
     463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380,
     973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665,
     874, 80, 45, 848, 38, 811, 267, 575]
c = [5, 2, 6, 1][::-1]
d = [1, 3, 2, 3, 1]
e = [7, 5, 6, 4]
print(Solution().reversePairs(a))
