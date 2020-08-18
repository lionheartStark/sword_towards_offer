"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        len_x = len(matrix)
        len_y = len(matrix[0])
        x = 0
        y = len_y - 1
        while True:
            if 0 <= x <= len_x - 1 and 0 <= y <= len_y - 1:
                if matrix[x][y] == target:
                    return True
                elif matrix[x][y] > target:
                    y -= 1
                else:
                    x += 1
            else:
                return False
