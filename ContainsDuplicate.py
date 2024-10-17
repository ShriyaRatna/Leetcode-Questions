class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
