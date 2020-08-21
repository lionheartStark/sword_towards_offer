from typing import List


class Solution:
    """
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        my solution
        :param nums:
        :return:
        """
        nums.sort()
        n = len(nums)
        res = []
        uesed = set()

        def get_it(first=0):
            # 终止条件
            if first == n:
                res.append(nums[:])
            else:
                a = str(nums[:first])
                if a in uesed:
                    print(a)
                    return
                else:
                    uesed.add(a)
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    # 继续递归填下一个数
                    get_it(first + 1)
                    # 撤销操作
                    nums[first], nums[i] = nums[i], nums[first]

        get_it()
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        self.res = []

        def dfs(num, subset):
            if not num:
                self.res.append(subset)
                return

            for i in range(len(num)):
                if i > 0 and num[i] == num[i - 1]:
                    continue
                dfs(num[:i] + num[i + 1:], subset + [num[i]])

        dfs(nums, [])
        return self.res


import pprint

ress = Solution().permuteUnique([1, 1, 1, 2])
print("------")
pprint.pprint(ress)
