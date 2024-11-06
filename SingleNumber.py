class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set(nums)
        for i in set1:
            if nums.count(i) == 1:
                return i
        return None