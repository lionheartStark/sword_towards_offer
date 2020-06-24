class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        if len(nums) == 0:
            return 0
        else:
            return max(dp)

    def lengthOfLIS_2FEN(self, nums: list) -> int:
        top_dp = [0] * len(nums)
        pil = 0

        for i in range(len(nums)):
            left = 0
            right = pil
            while left < right:
                mid = (left+right) // 2
                if nums[mid] < nums[i]:
                    left = mid+1
                elif nums[mid] > nums[i]:
                    right = mid-1
                else:
                    left = mid

            top_dp[left] = nums[i]
            if left == pil:
                pil += 1
        return pil
