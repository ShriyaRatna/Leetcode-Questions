class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums = set(nums1)
        for i in nums1:
            if i in nums2 and i in nums:
                nums.remove(i)

        ans = []
        ans.append(list(nums))

        nums = set(nums2)
        for i in nums2:
            if i in nums1 and i in nums:
                nums.remove(i)

        ans.append(list(nums))

        return ans
