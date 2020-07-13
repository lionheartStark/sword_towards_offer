from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        给定两个数组，编写一个函数来计算它们的交集。

        :param nums1:
        :param nums2:
        :return:
        """
        count_1 = collections.Counter(nums1)
        count_2 = collections.Counter(nums2)
        res = []
        for k in count_1:
            if k in count_2:
                need_extend = [k] * min(count_1[k], count_2[k])
                res.extend(need_extend)
        return res
print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))