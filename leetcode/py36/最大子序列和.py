class Solution:
    def maxSubArray(self, nums: list) -> int:
        asum = [0]*(len(nums))
        asum[0] = nums[0]
        for i in range(1, len(nums)):
            asum[i] = nums[i] + asum[i-1]
        amax = None
        minqian= None
        for i in range(len(asum)):
            if i == 0:
                amax = asum[0]
                minqian = min(asum[0], 0)
            else:
                amax = max(asum[i]-minqian, amax)
                minqian = min(minqian, asum[i])
        return amax

print(Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))