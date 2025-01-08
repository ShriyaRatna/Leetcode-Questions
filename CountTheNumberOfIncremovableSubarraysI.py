class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            new = nums.copy()
            while len(new) != 1 and len(new) > i:
                new.pop(i)
                if new == sorted(list(set(new))):
                    ans += 1
        return ans + 1
