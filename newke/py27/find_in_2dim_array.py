# -*- coding:utf-8 -*-
class Solution:
    """
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
    输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    TODO(warn):这个题目告诉我们在做python题目的时候要考虑空数组的情况
    """
    # array 二维列表
    def Find(self, target, array):
        """
        这个方法是最愚蠢的正确解决方法
        :param target:
        :param array:
        :return:
        """
        for i in array:
            if target in i:
                return True
        return False
        # write code here

    def Find(self, target, array):
        """
        这个方法是比较聪明的正确解决方法
        :param target:
        :param array:
        :return:
        """
        lie_find = []
        for i in array:
            if i:
                if target > i[-1]:
                    pass
                else:
                    lie_find.append(i)
            else:
                return False

        if lie_find:
            hang_idx = len(lie_find[0])-1
            for i in range(len(lie_find[0])):
                if target > lie_find[i][hang_idx]:
                    continue
                else:
                    for hang in range(hang_idx+1):
                        if target == lie_find[i][hang]:
                            return True

        else:
            return False

        return False
        # write code here


if __name__ == "__main__":
    res = Solution().Find(15,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
    print(res)