from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = 0
        max_key = None
        for i in count:
            if count[i] > max_count:
                max_count = count[i]
                max_key = i
        return max_key


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
