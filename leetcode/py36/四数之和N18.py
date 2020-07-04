from typing import List


class Solution:
    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
        """
        三数之和
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(len(nums)):
            # 避免重复
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # a+b+c = target
            a = nums[i]
            sum2_target = target - a
            end = n - 1
            for start in range(i + 1, n):
                if start > i + 1 and nums[start] == nums[start - 1]:
                    continue
                else:
                    while start < end and nums[start] + nums[end] > sum2_target:
                        end -= 1
                    # 防止指针越界
                    if start >= end:
                        break
                    if nums[start] + nums[end] == sum2_target:
                        res.append([a, nums[start], nums[end]])
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        4数之和
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(len(nums)):
            # 避免重复
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # a+b+c = target
            a = nums[i]
            sum3_target = target - a

            # 开始求三数之和
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                b = nums[j]
                sum2_target = sum3_target - b
                # 开始求俩数和
                end = n - 1
                for start in range(j +1, n):
                    if start > j + 1 and nums[start] == nums[start - 1]:
                        continue

                    else:
                        while start < end and nums[start] + nums[end] > sum2_target:
                            end -= 1
                        # 防止指针越界
                        if start >= end:
                            break
                        if nums[start] + nums[end] == sum2_target:
                            res.append([a, b, nums[start], nums[end]])
        return res

nums =[1, 0, -1, 0, -2, 2]
print(Solution().fourSum(nums, 0))
