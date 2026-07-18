from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        return max(count, key=count.get)