class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        prev = 0
        for i in range(k):
            prev += nums[i]
        max = float(prev)
        for i in range(k, len(nums)):
            prev = prev + float(nums[i]) - float(nums[i - k])
            if prev > max:
                max = prev

        return max / k
