from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = dict(Counter(nums))
        # return max(count, key=count.get)

        res, count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        
        return res