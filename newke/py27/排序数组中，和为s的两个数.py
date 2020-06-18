# -*- coding:utf-8 -*-

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
        输入一个递增排序的数组和一个数字S，在数组中查找两个数，
        使得他们的和正好是S，如果有多对数字的和等于S，
        输出两个数的乘积最小的。
        """
        # write code here
        res_list = []
        low = 0
        high = len(array)-1
        while True:
            if low >= high:
                break
            sum = array[low] + array[high]
            if sum < tsum:
                low += 1
            elif sum == tsum:
                res_list.append([array[low],array[high]])
                return [array[low], array[high]]
                # low += 1
                # high -= 1
                # if low > high:
                #     break
            elif sum > tsum:
                high -=1
        return []