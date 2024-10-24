class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 2:
            profit = [0] * len(nums)
            profit[0] = nums[0]
            profit[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])
            return profit[len(nums) - 1]
        else:
            return max(nums)
