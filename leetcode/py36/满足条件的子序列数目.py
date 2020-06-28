import bisect
mod = 1E9 +7

class Solution:
    def numSubseq(self, nums: list, target: int) -> int:
        """
        排序加二分加快速幂， just so so
        """
        nums.sort()
        lens = len(nums)
        #print(nums)
        res = 0
        for i in range(lens):
            my = nums[i]
            x = target - my
            j = bisect.bisect_right(nums, x)-1
            if j >= i:
                res = (res+2**(j-i)) % mod
        return int(res)



    def numSubseq2(self, nums: list, target: int) -> int:
        """
        排序加双指针，best
        """
        nums.sort()
        if nums[0] * 2 > target:
            return 0

        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                res += 2 ** (right - left)
                left += 1
            else:
                right -= 1
        return res % (10 ** 9 + 7)

    def my_2fen_sort_right(self, the_list, x):

        pass

print(Solution().numSubseq([5,2,4,1,7,6,8],16)) # 127
print(Solution().numSubseq([3, 3, 6, 8], 10))