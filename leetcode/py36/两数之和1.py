class Solution:
    def twoSumBest(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            want = target - nums[i]
            if want in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(want)]
            else:
                continue


print(Solution().twoSumBest([2, 2], 4))
