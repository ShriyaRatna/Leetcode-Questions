class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        for i in nums:
            if i not in stack:
                stack.append(i)
        for i in range(len(stack)):
            nums[i] = stack[i]

        return len(stack)
