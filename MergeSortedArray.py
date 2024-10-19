class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        c1 = 0
        c2 = 0
        while c1 < m and c2 < n:
            if nums1[c1] <= nums2[c2]:
                ans.append(nums1[c1])
                c1 += 1
            else:
                ans.append(nums2[c2])
                c2 += 1
        while c1 < m:
            ans.append(nums1[c1])
            c1 += 1
        while c2 < n:
            ans.append(nums2[c2])
            c2 += 1

        # nums1 = ans
        for i in range(len(ans)):
            nums1[i] = ans[i]
