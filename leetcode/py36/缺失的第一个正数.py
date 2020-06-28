class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        """
        不满足题目要求
        """
        nums.sort()
        want = 1
        for i in range(0, len(nums)):
            if nums[i] == want:
                want += 1
            elif want < nums[i]:
                return want
        return want

    def firstMissingPositive(self, nums: list) -> int:
        """
        置换方法
        """
        len_nums = len(nums)
        for i in range(len_nums):
            while 1 <= nums[i] <= len_nums and nums[i] != nums[nums[i] - 1]:
                c = nums[i]
                nums[i] = nums[c - 1]
                nums[c - 1] = c

        for i in range(len_nums):
            if nums[i] != i + 1:
                return i + 1
        return len_nums + 1


print(Solution().firstMissingPositive([3, 4, -1, 1]))
