from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] == i+1:
                nums[i] = -nums[i]
            else:
                # 补位写法也是对的
                # now = nums[i]
                # while now > 0:
                #     tmp = nums[now-1]
                #     if tmp < 0:
                #         break
                #     nums[now - 1] = -now
                #     now = tmp
                # if nums[i] > 0:
                #     nums[i] = now

                # 交换写法
                while nums[i] > 0:
                    tmp = nums[nums[i] - 1]
                    if tmp < 0:
                        break
                    nums[nums[i] - 1] = -nums[i]
                    if nums[i] > 0:
                        nums[i] = tmp
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        print(nums)
        print(res)
        return res

Solution().findDisappearedNumbers([2,1])