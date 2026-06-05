class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #not O(1) space
        # counter_nums = Counter(nums)
        # return max(counter_nums, key = counter_nums.get)

        #not a linked list but treat list array as linked list to find dupes

        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slower = 0

        while True:
            slow = nums[slow]
            slower = nums[slower]
            if slow == slower:
                return slow