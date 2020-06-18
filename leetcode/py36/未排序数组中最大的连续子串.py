class Solution:

    def __init__(self):
        self.max = 1

    def find_qian_and_hou(self, num, nums):
        qian = num - 1
        hou = num + 1
        tmp = 1
        while qian in nums:
            tmp += 1
            nums.remove(qian)
            qian -= 1
        while hou in nums:
            tmp += 1
            nums.remove(hou)
            hou += 1
        if self.max < tmp:
            self.max = tmp
        nums.remove(num)

    def longestConsecutive(self, nums):
        nums = set(nums)
        while nums:
            for num in nums:
                self.find_qian_and_hou(num, nums)
                break
        print(self.max)
        return self.max

Solution().longestConsecutive([100, 4, 200, 1, 3, 2])