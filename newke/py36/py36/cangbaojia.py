from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(list(enumerate(nums)))
        if not nums:
            return -1
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # #
            # if nums[mid] == nums[r] and nums[mid] == nums[l]:
            #     l += 1
            #     r -= 1
            elif nums[mid] <= nums[r]:
                if nums[mid+1] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid -1
            else:
                if nums[l] <= target <= nums[mid-1]:
                    r = mid -1
                else:
                    l = mid+1

        return -1
a = [4,5,6,7,0,1,2]
b = 0
print(Solution().search(a,b))