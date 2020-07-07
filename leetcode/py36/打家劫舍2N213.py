class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

    def rob(self, nums) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        nums1 = nums[:n-1]
        max1 = self.rob1(nums1)
        nums2 = nums[1:n]
        max2 = self.rob1(nums2)
        return max(max1, max2)
