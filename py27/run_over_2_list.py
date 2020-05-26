# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        """
        TODO:这玩意我不会写了
        """
        print_list = []
        i = 0
        j = 0
        if matrix == [] or matrix[0] == []:
            return []
        else:
            print(matrix[0])
            matrix.pop(0)

            print("----")
            for i in matrix:
                if len(i)-1 >= 0:
                    print(i[len(i)-1])
                    i.pop(len(i)-1)
                else:
                    return
            print("----")



Solution().printMatrix([[1, 2]])