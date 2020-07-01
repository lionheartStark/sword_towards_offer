class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()

        ans = None

        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = length - 1
            while left < right:
                sum = nums[i] + nums[right] + nums[left]

                if ans == None:
                    ans = sum
                else:
                    if abs(sum - target) < abs(ans - target):
                        ans = sum

                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return ans
