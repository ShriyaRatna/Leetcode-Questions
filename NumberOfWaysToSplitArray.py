class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        right = sum(nums) - left
        if left >= right:
            ans = 1
        for i in range(1, len(nums)-1):
            left = left + nums[i]
            right = right - nums[i]
            if left >= right:
                ans = ans + 1
        
        return ans