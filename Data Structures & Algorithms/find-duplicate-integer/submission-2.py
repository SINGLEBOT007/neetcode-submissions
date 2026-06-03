class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)

        return max(counter_nums, key = counter_nums.get)
        