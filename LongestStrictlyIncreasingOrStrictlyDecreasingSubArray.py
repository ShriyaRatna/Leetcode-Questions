class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count = 1
        maxi = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
            else:
                maxi = max(count, maxi)
                count = 1

        maxi = max(count, maxi)
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                maxi = max(count, maxi)
                count = 1

        return max(maxi, count)
