import numpy as np

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = int(np.median(nums))
        ans = 0
        for i in nums:
            ans += abs(i-median)

        return ans