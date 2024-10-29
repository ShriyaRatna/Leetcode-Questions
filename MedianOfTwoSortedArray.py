class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = n = 0
        ans = []
        while m < len(nums1) and n < len(nums2):
            if nums1[m] > nums2[n]:
                ans.append(nums2[n])
                n += 1
            else:
                ans.append(nums1[m])
                m += 1
        while m < len(nums1):
            ans.append(nums1[m])
            m += 1

        while n < len(nums2):
            ans.append(nums2[n])
            n += 1

        if len(ans) % 2 == 1:
            return ans[len(ans) // 2]
        else:
            return (float(ans[len(ans) // 2 - 1]) + float(ans[len(ans) // 2])) / 2
