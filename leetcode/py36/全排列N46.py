from typing import List


class Solution:

    def get_pailie(self, now, nums):
        if not nums:
            self.res.append(now)
        else:
            for i in nums:
                new_nums = nums[:]
                new_nums.remove(i)
                self.get_pailie(now + [i], new_nums)

    def mypermute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        self.get_pailie([], nums)

        return self.res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


print(Solution().permute([1, 2, 3]))
